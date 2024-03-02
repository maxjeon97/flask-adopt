import os
import requests
from random import choice

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']

PETFINDER_API = 'https://api.petfinder.com/v2'

def update_auth_token_string():
    resp = requests.post(f'{PETFINDER_API}/oauth2/token',
                        data={
                            "grant_type": "client_credentials",
                            "client_id": API_KEY,
                            "client_secret": API_SECRET
                        })
    token = resp.json()

    return token["access_token"]


def get_pet_finder_info(token):
    resp = requests.get(f'{PETFINDER_API}/animals?limit=100',
                        headers={
                            'Authorization': f'Bearer {token}'
                        })
    animals = resp.json()['animals']
    animal = choice(animals)
    return {
        'name': animal['name'],
        'age': animal['age'],
        'photo_url': animal['photos'][0]['medium']
    }