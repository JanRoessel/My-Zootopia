import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals?name="


def fetch_animals(animal_name):
    url = API_URL + animal_name

    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("API Fehler:", response.status_code, response.text)
        return []
    return response.json()


def serialize_animal(animal_obj):
    name = animal_obj.get("name", "Unknown")
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", None)

    html = '<li class="cards__item">\n'
    html += f'<div class="card__title">{name}</div>\n'
    html += '<p class="card__text">\n'
    html += f'<strong>Diet:</strong> {diet}<br/>\n'

    if locations:
        html += f'<strong>Location:</strong> {", ".join(locations)}<br/>\n'

    if animal_type:
        html += f'<strong>Type:</strong> {animal_type}<br/>\n'

    html += '</p>\n'
    html += '</li>\n'
    return html


def generate_animals_string(animals):
    if not animals:
        return "<li>No animals found.</li>"

    return "".join(serialize_animal(a) for a in animals)


def write_html(content, output_file="animals.html"):
    with open(output_file, "w") as file:
        file.write(content)


def main():
    animal_name = input(" Which animal are you looking for? ")

    print("\nFetching from API...\n")

    animals = fetch_animals(animal_name)

    print(f"Found {len(animals)} result(s)\n")

    with open("animals_template.html", "r") as file:
        template = file.read()

    animals_html = generate_animals_string(animals)

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_html)

    write_html(final_html)

    print(" animals.html generated successfully")


if __name__ == "__main__":
    main()