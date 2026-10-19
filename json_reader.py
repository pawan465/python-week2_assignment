"""Assignment 3: load JSON data and print it in a readable format."""

import json

file_name = input("Enter the name or path of a JSON file: ").strip()

try:
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Indentation makes nested JSON easier to read.
    print("JSON data:")
    print(json.dumps(data, indent=4, ensure_ascii=False))

except FileNotFoundError:
    print("File not found. Check the file name and try again.")
except json.JSONDecodeError as error:
    print(f"The file does not contain valid JSON: {error}")
except OSError as error:
    print(f"Could not read the file: {error}")
