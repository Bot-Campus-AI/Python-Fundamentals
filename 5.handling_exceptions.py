import json

try:
    with open('nonexistent.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except json.JSONDecodeError:
    print("An error occurred while decoding the JSON data.")
