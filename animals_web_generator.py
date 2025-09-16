import json

# Step 1: Load animal data from JSON
def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


# Step 2: Read the template HTML file
def load_template(template_path):
    with open(template_path, "r") as f:
        return f.read()


# Step 3: Generate the HTML string with animal info (only if data exists)
def generate_animal_info(data):
    output = ''  # define an empty string
    for block in data:
        # append information to each string
        output += '<li class="cards__item">'

        if block.get("name"):
            output += f"Name: {block['name']}<br/>\n"

        if block.get("characteristics", {}).get("diet"):
            output += f"Diet: {block['characteristics']['diet']}<br/>\n"

        if block.get("locations") and len(block["locations"]) > 0:
            output += f"Location: {block['locations'][0]}<br/>\n"

        if block.get("characteristics", {}).get("type"):
            output += f"Type: {block['characteristics']['type']}<br/>\n"

        #output += "<br>\n"  # spacing between animals
        output += '</li>'
    return output

# Step 4: Replace the placeholder with actual content
def create_final_html(template_str, animals_html):
    return template_str.replace("__REPLACE_ANIMALS_INFO__", animals_html)


# Step 5: Write the result to animals.html
def write_output(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)

if __name__ == "__main__":
    animals_data = load_data("animals_data.json")
    template_html = load_template("animals_template.html")
    animal_info_html = generate_animal_info(animals_data)
    final_html = create_final_html(template_html, animal_info_html)
    write_output("animals.html", final_html)

    print("animals.html generated successfully.")


