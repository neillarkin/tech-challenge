import os
from flask import Flask, render_template, request, url_for
import requests, json

app = Flask(__name__)

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_SPECIES_API_URL = "https://pokeapi.co/api/v2/pokemon-species/"
TRANSLATION_API_URL = "https://api.funtranslations.com/translate/shakespeare.json?text="


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    error = None
    description = None
    query = request.args['search']
    query_url = POKEMON_API_URL + query

    if not query:
        error = "Enter a character name"
    elif query:
        query_response = requests.get(query_url)
        if query_response.status_code != 200:
            error = str(query_response.status_code) + " Nothing Found"
        else:
            dict = query_response.json()
            error = str(dict['name'])
            query_url = POKEMON_SPECIES_API_URL + error
            query_response = requests.get(query_url)
            dict.clear()
            dict = query_response.json()
            flavor_entries = dict['flavor_text_entries']
            flavor_text = flavor_entries[0]
            description = str(flavor_text['flavor_text'])

    return render_template('index.html', error=error, description=description)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
