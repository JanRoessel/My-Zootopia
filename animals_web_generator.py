from data_fetcher import fetch_data


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


def generate_html(animals):
    if not animals:
        return "<li>No animals found.</li>"

    return "".join(serialize_animal(a) for a in animals)


def write_html(content, output_file="animals.html"):
    with open(output_file, "w") as file:
        file.write(content)


def main():
    animal_name = input(" Which animal are you looking for? ")

    animals = fetch_data(animal_name)

    if not animals:
        print(f" No results found for '{animal_name}'")
        return

    print(f"Found {len(animals)} result(s)")

    with open("animals_template.html", "r") as file:
        template = file.read()

    html_block = generate_html(animals)

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", html_block)

    write_html(final_html)

    print(" animals.html generated successfully")


if __name__ == "__main__":
    main()