import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for block in animals_data:
    if block.get("name"):
        print(f"Name: {block['name']}")
    if block["characteristics"].get("diet"):
        print(f"Diet: {block['characteristics']['diet']}")
    if block["locations"]:
        print(f"Location: {block['locations'][0]}")
    if block["characteristics"].get("type"):
        print(f"Type: {block['characteristics']['type']}")
    print("*" * 50)


