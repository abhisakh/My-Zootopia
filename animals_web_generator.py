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

# Step Added later: Single animal serialization
def serialize_animal(animal_obj, indent=4):
    """
    Generate an indented HTML string containing single animal information.

    Args:
        Single data part from json file (one animal)
        indent (int): Number of spaces to use for base indentation.

    Returns:
        str: Generated HTML string with animal cards(single animal).
    """
    output = ''  # define an empty string

    outer_space = ' ' * indent  # 4 spaces, e.g., '    '
    space = 2 * outer_space      # 8 spaces
    inner_space = 2 * space      # 16 spaces

    output += f'{outer_space}<li class="cards__item">\n'

    if animal_obj.get("name"):
        output += f'{space}<div class="card__title">'
        output += f" {animal_obj['name']}"
        output += '</div><br/>\n'
        output += f'{space}<p class="card__text">\n'

    if animal_obj.get("characteristics", {}).get("diet"):
        output += f'{inner_space}<strong>Diet:</strong>'
        output += f" {animal_obj['characteristics']['diet']}<br/>\n"

    if animal_obj.get("locations") and len(animal_obj["locations"]) > 0:
        output += f'{inner_space}<strong>Location:</strong>'
        output += f" {animal_obj['locations'][0]}<br/>\n"

    if animal_obj.get("characteristics", {}).get("type"):
        output += f'{inner_space}<strong>Type:</strong>'
        output += f" {animal_obj['characteristics']['type']}<br/>\n"

    output += f'{space}</p>\n'
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


'''
# Step 3: Generate the HTML string with animal info (only if data exists)
def generate_animal_info(data, indent=4):
    """
    Generate an indented HTML string containing animal information.

    Args:
        data (list): List of dictionaries with animal data.
        indent (int): Number of spaces to use for base indentation.

    Returns:
        str: Generated HTML string with animal cards.
    """
    output = ''  # define an empty string

    outer_space = ' ' * indent  # 4 spaces, e.g., '    '
    space = 2 * outer_space      # 8 spaces
    inner_space = 2 * space      # 16 spaces

    for block in data:
        output += f'{outer_space}<li class="cards__item">\n'

        if block.get("name"):
            output += f'{space}<div class="card__title">'
            output += f" {block['name']}"
            output += '</div><br/>\n'
            output += f'{space}<p class="card__text">\n'

        if block.get("characteristics", {}).get("diet"):
            output += f'{inner_space}<strong>Diet:</strong>'
            output += f" {block['characteristics']['diet']}<br/>\n"

        if block.get("locations") and len(block["locations"]) > 0:
            output += f'{inner_space}<strong>Location:</strong>'
            output += f" {block['locations'][0]}<br/>\n"

        if block.get("characteristics", {}).get("type"):
            output += f'{inner_space}<strong>Type:</strong>'
            output += f" {block['characteristics']['type']}<br/>\n"

        output += f'{space}</p>\n'
        output += f'{outer_space}</li>\n\n'

    return output
'''

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
