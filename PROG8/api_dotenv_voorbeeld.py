# Requests voor het versturen van HTTP verzoeken
from textwrap import indent

import requests

# Hulp library voor JSON
import json

# Importeer dotenv om API key te beschermen
from dotenv import load_dotenv
import os

# Bee movie ID
beemovie = "tt0389790"

# Load environment variables from the .env file (if present)
load_dotenv()

def get_key():
    """ Get the API key from the .env """
    # Access environment variables as if they came from the actual environment
    apikey = os.getenv('API_KEY')

    # Example usage
    print(f'API key length: {len(apikey)}')

    return apikey

# Basis URL voor een IMDB ID om film te vinden
url = f"https://www.omdbapi.com/?i={beemovie}&apikey={get_key()}"

# Stuur het verzoek via HTTP naar de OMDB servers
r = requests.get(url)

if r.status_code == 200:
    print("Verzoek gelukt!")
    # Formatteer de output en laat zien
    print(json.dumps(r.json(), indent=3))
else:
    print("Verzoek niet gelukt :(")
    print(f"Status code: {r.status_code}")