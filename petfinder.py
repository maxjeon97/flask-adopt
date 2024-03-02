import os
import requests

API_KEY = os.environ['API_KEY']
API_SECRET = os.environ['API_SECRET']

PETFINDER_API = 'https://api.petfinder.com/v2'

def update_auth_token_string():
    resp = requests.post(f'{PETFINDER_API}/oauth2/token',
                        data={
                            "grant-type": "client_credentials",
                            "client_id": API_KEY,
                            "client_secret": API_SECRET
                        })
    token = resp.json()

    return token["access_token"]


