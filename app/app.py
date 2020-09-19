import os
from flask import Flask, render_template, request, url_for
import requests, json
app = Flask(__name__)

url = "https://pokeapi.co/api/v2/pokemon/"
param = "ditto"
url2 = "https://pokeapi.co/api/v2/pokemon-species/6/"



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    query = request.args['search']
    result = url + query
    response = requests.get(result)
    dict = response.json()
    species_array = dict['species']
    species_url = species_array['url']

    response = requests.get(species_url)
    dict = response.json()
    return render_template('index.html', species_url=species_url, data=dict)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)