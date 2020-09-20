import os
from flask import Flask, request, render_template, url_for, jsonify, redirect
import requests, json

app = Flask(__name__)
url = "https://pokeapi.co/api/v2/pokemon/"
url2 = "https://pokeapi.co/api/v2/pokemon-species/"
url3 = "https://api.funtranslations.com/translate/shakespeare.json?text="


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    query = request.args['search']
    result = url + query
    response1 = requests.get(result)
    dict = response1.json()
    name = str(dict['name'])
    result2 = url2 + name
    response2 = requests.get(result2)
    dict.clear()
    dict = response2.json()
    flavor_entries = dict ['flavor_text_entries']
    flavor_text = flavor_entries[0]
    description = str(flavor_text['flavor_text'])
    return render_template('index.html', name=name, result=result, result2=result2, description=description)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
