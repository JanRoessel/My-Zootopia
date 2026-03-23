import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")
print(animals_data)

for dic in animals_data:
    print(f"Name: {dic["name"]}")
    print(f"Diet: {dic["characteristics"]["diet"]}")
    print(f"Location: {", ".join(dic["locations"])}")
    if dic["characteristics"].get("type") != None:
        print(f"Type: {dic["characteristics"].get("type")}")
    print()

with open("animals_template.html", "r") as file:
    html_content = file.read()

animals_string = ""
for animal in animals_data:
    animals_string += "<li class='cards__item'>"
    animals_string += f"<div class='card__title'>{animal['name']}</div>"
    animals_string += "<div class='card__text'>"
    animals_string += f"<p>Diet: {animal['characteristics']['diet']}</p>"
    animals_string += f"<p>Location: {', '.join(animal['locations'])}</p>"
    if animal['characteristics'].get('type'):
        animals_string += f"<p>Type: {animal['characteristics']['type']}</p>"
    animals_string += "</div>"
    animals_string += "</li>"

new_html = html_content.replace("__REPLACE_ANIMALS_INFO__", animals_string)

with open("animals.html", "w") as file:
    file.write(new_html)
