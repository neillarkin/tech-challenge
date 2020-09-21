import os
from flask import Flask, flash, request, render_template, url_for
import requests, json
from tests import *

app = Flask(__name__)
POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"
POKEMON_SPECIES_API_URL = "https://pokeapi.co/api/v2/pokemon-species/"
TRANSLATION_API_URL = "https://api.funtranslations.com/translate/shakespeare.json?text="

@app.route('/')
def index():
    return render_template('index.html')


"""Search query is used to get JSON responses for both pokeapi URLS."""
@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    placeholder = None
    translation = None
    description = None
    query = request.args['search'].lower()
    query_url = POKEMON_API_URL + query

    if not query:
        placeholder = "Enter a character name"

    if query:
        query_response = requests.get(query_url)
        if query_response.status_code != 200:
            placeholder = str(query_response.status_code) + " Nothing Found"
        else:
            dict = query_response.json()
            placeholder = str(dict['name'])
            query_url = POKEMON_SPECIES_API_URL + placeholder
            query_response = requests.get(query_url)
            dict.clear()
            dict = query_response.json()
            description = getDescription(dict['flavor_text_entries'])
            translation_param = {'text': str(description)}
            translation = postTranslation(translation_param)
            # translation = "This is temporary text to prevent 429 response"
    return render_template('index.html', placeholder=placeholder, description=description, translation=translation)


""" Check if the JSON key value in English and return if true."""
def getDescription(flavor_text_entries):
    for entry in flavor_text_entries:        
        if entry['language']['name'] == 'en':
            description = entry['flavor_text']
            return description


""" Send poekmon description to Shakespearean translator."""
@app.route('/shakespeare', methods=['POST'])
def postTranslation(text):
    query_response = requests.post(TRANSLATION_API_URL, data=text)
    if query_response.status_code == 429:
        dict = query_response.json()
        text = dict['placeholder']['message']
        return text
    else:
        dict = query_response.json()
        text = dict['contents']['translated']
        return text


""" Tests if Pokeapi.co is responding with either 200 or 500 codes """
def testConnection(name):
    url = POKEMON_API_URL + name
    response = requests.get(url)
    status = str(response.status_code)
    return status

test_are_equal(testConnection('ditto'),'200' )
test_not_equal(testConnection('ditto'),'500' )


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
