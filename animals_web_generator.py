import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialize a single animal to a HTML string"""
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'
    output += f'<strong>Location:</strong> {", ".join(animal_obj["locations"])}<br/>\n'
    if animal_obj["characteristics"].get("type"):
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output


def generate_animals_string(animals_data):
    """Generate HTML string for all animals"""
    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    return output

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r") as file:
        html_content = file.read()

    animals_string = generate_animals_string(animals_data)
    new_html = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    with open("animals.html", "w") as file:
        file.write(new_html)