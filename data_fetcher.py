import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals
    """
    url = API_URL + animal_name
    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("API Error:", response.status_code, response.text)
        return []

    return response.json()