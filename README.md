# 🐾 Animal Info Web Generator
This project is a simple Python application that dynamically generates an HTML webpage 
displaying animal information. Users can choose to filter animals by their skin_type 
(e.g., Hair, Scales, Feathers), or view all animals at once. All animal data is sourced 
from a structured JSON file.

## 🗂️ Project Structure
```text
project/
│
├── animals_data.json           # JSON file containing animal data
├── animals_template.html       # HTML template with a placeholder
├── animals_web_generator.py    # Main Python script
├── animals.html                # Generated HTML output (auto-created)
└── instruction.txt             # Instructions on how we constructed the project
```

## 🚀 Features
- 🔍 Filter by skin_type: Choose a skin type from a generated list to view only 
  matching animals.
- 🧩 Handle missing data: Animals without a skin_type are labeled as "Unknown".
- 🌐 Auto-generate HTML: The script outputs a polished HTML file with animal cards.
- 🐍 PEP8-compliant: Clean and readable Python code.
- 📄 Modular codebase: Functions are cleanly separated for data loading, filtering, 
and HTML generation.

## 📌 How It Works
- The script reads data from animals_data.json.
- It extracts all unique skin_type values and displays them to the user 
  (including Unknown and All).
- The user selects a skin type via console input.
- Only matching animals are used to generate the HTML.(in case All is chosen
  then no filtering)
- The final webpage (animals.html) is saved and can be opened in any browser.

## 🛠️ Requirements
- Python 3.x
- No external libraries required

## ▶️ Running the Project
Make sure all files are in the same directory, then run:
```text
python animals_web_generator.py
```
Follow the on-screen prompt to choose a skin_type, and the HTML file will be generated in the same folder.

## 📄 JSON File Format
Each animal entry in animals_data.json follows this structure:
```text
{
  "name": "American Foxhound",
  "locations": ["North America"],
  "characteristics": {
    "diet": "Omnivore",
    "type": "Mammal",
    "skin_type": "Hair"
  }
}
```
### 👤 Author

- **Abhisakh Sarma** - [GitHub Profile]((https://github.com/abhisakh)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

