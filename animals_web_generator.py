import json


def load_data(file_path):
    """Load data from a JSON file."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_template(template_path):
    """Load the HTML template file as a string."""
    with open(template_path, "r") as f:
        return f.read()


def serialize_animal(animal_obj, indent=4):
    """Generate an indented HTML string containing single animal information."""
    output = ''
    outer_space = ' ' * indent
    space = ' ' * (indent * 2)
    inner_space = ' ' * (indent * 3)
    detail_space = ' ' * (indent * 4)

    output += f'{outer_space}<li class="cards__item">\n'

    if animal_obj.get("name"):
        output += (
            f'{space}<div class="card__title">'
            f'{animal_obj["name"]}</div>\n'
        )

    output += f'{space}<div class="card__text">\n'
    output += f'{inner_space}<ul class="card__details">\n'

    diet = animal_obj.get("characteristics", {}).get("diet")
    if diet:
        output += (
            f'{detail_space}<li class="card__details-item">'
            f'<strong>Diet:</strong> {diet}</li>\n'
        )

    locations = animal_obj.get("locations")
    if locations:
        output += (
            f'{detail_space}<li class="card__details-item">'
            f'<strong>Location:</strong> {locations[0]}</li>\n'
        )

    animal_type = animal_obj.get("characteristics", {}).get("type")
    if animal_type:
        output += (
            f'{detail_space}<li class="card__details-item">'
            f'<strong>Type:</strong> {animal_type}</li>\n'
        )

    output += f'{inner_space}</ul>\n'
    output += f'{space}</div>\n'
    output += f'{outer_space}</li>\n\n'

    return output


def generate_animal_info(data):
    """Generate an indented HTML string containing animal information."""
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj, indent=4)
    return output


def create_final_html(template_str, animals_html):
    """Replace placeholder in template with generated animal HTML."""
    return template_str.replace("__REPLACE_ANIMALS_INFO__", animals_html)


def write_output(file_path, content):
    """Write content to a file."""
    with open(file_path, "w") as f:
        f.write(content)


def get_unique_skin_types(data):
    """
    Extract unique skin_type values from animals data.
    Animals missing skin_type are treated as 'Unknown'.
    Adds 'All' to the beginning of the list.
    """
    skin_types = set()
    for animal in data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if not skin_type:
            skin_type = "Unknown"
        skin_types.add(skin_type)
    return ["All"] + sorted(skin_types)


def filter_animals_by_skin_type(data, selected_skin_type):
    """
    Filter animal list by selected skin_type.
    Returns all animals if 'All' is selected.
    """
    if selected_skin_type == "All":
        return data

    filtered = []
    for animal in data:
        skin_type = animal.get("characteristics", {}).get("skin_type")
        if not skin_type:
            skin_type = "Unknown"
        if skin_type == selected_skin_type:
            filtered.append(animal)
    return filtered


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    skin_type_list = get_unique_skin_types(animals_data)

    print("Available skin_type values:")
    for idx, skin_type in enumerate(skin_type_list, 1):
        print(f"{idx}. {skin_type}")

    while True:
        user_input = input("Enter a skin_type from the list above (or 'All' to show all animals): ").strip()
        if user_input in skin_type_list:
            break
        else:
            print("Invalid input. Please enter a valid skin_type from the list.")

    filtered_animals = filter_animals_by_skin_type(animals_data, user_input)

    template_html = load_template("animals_template.html")
    animal_info_html = generate_animal_info(filtered_animals)
    final_html = create_final_html(template_html, animal_info_html)
    write_output("animals.html", final_html)

    print(f"animals.html generated successfully for skin_type: {user_input}")

