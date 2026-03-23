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


#Name: American Foxhound
#Diet: Omnivore
#Location: North-America
#Type: Hound
