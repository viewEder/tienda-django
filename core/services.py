import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_pokemon(params={}):
    url = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0'
    response = generate_request(url, params)
    if response:
       poquemon = response.get('results')[0]
       return poquemon.get('name').get('first')

    return ''"
