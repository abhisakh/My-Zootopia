import json


# Step 1: Load animal data from JSON
def load_data(file_path):
    """
    Load data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list or dict: Parsed JSON data.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Step 2: Read the template HTML file
def load_template(template_path):
    """
    Load the HTML template file as a string.

    Args:
        template_path (str): Path to the template HTML file.

    Returns:
        str: Template file content.
    """
    with open(template_path, "r") as f:
        return f.read()

def serialize_animal(animal_obj, indent=4):
    """
    Generate an indented HTML string containing single animal information.

    Args:
        animal_obj (dict): Single animal dictionary.
        indent (int): Number of spaces to use for base indentation.

    Returns:
        str: HTML string for a single animal card.
    """
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

# Step 3: Generate the HTML string with animal info (only if data exists)
def generate_animal_info(data):
    """
    Generate an indented HTML string containing animal information.
    Use serialize_animal(animal_obj, indent=4) inside

    Args:
        data (list): List of dictionaries with animal data.
        indent (int): Number of spaces to use for base indentation.

    Returns:
        str: Generated HTML string with animal cards.
    """
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj, indent=4)
    return output

# Step 4: Replace the placeholder with actual content
def create_final_html(template_str, animals_html):
    """
    Replace placeholder in template with generated animal HTML.

    Args:
        template_str (str): The HTML template string.
        animals_html (str): The generated HTML string for animals.

    Returns:
        str: Final HTML with animal info inserted.
    """
    return template_str.replace("__REPLACE_ANIMALS_INFO__", animals_html)


# Step 5: Write the result to animals.html
def write_output(file_path, content):
    """
    Write content to a file.

    Args:
        file_path (str): Path to the output file.
        content (str): Content to write.
    """
    with open(file_path, "w") as f:
        f.write(content)


if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    template_html = load_template("animals_template.html")
    animal_info_html = generate_animal_info(animals_data)
    final_html = create_final_html(template_html, animal_info_html)
    write_output("animals.html", final_html)

    print("animals.html generated successfully.")
