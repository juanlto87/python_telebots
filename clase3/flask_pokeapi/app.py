from flask import Flask, render_template, request
import requests
import math

app = Flask(__name__)

POKEMONS_PER_PAGE = 9

@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '').lower()
    page = int(request.args.get('page', 1))

    offset = (page - 1) * POKEMONS_PER_PAGE
    url = f'https://pokeapi.co/api/v2/pokemon?limit={POKEMONS_PER_PAGE}&offset={offset}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Error al obtener los Pokémon"

    results = response.json()
    all_pokemon = []

    for poke in results['results']:
        poke_data = requests.get(poke['url']).json()
        name = poke_data['name']

        if search_query in name:
            pokemon = {
                'name': name.upper(),
                'sprite': poke_data['sprites']['front_default'],
                'image': poke_data['sprites']['other']['official-artwork']['front_shiny'],
                'types': [t['type']['name'] for t in poke_data['types']],
                'height': poke_data['height'],
                'weight': poke_data['weight'],
                'abilities': [a['ability']['name'] for a in poke_data['abilities']]
            }
            all_pokemon.append(pokemon)

    total = 100  
    total_pages = math.ceil(total / POKEMONS_PER_PAGE)

    return render_template('index.html', 
                           pokemon_list=all_pokemon,
                           search_query=search_query,
                           page=page,
                           total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
