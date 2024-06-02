
import json

# Load the JSON data from the file
with open('example.json', 'r') as file:
    data = json.load(file)

# Iterate over the list of dictionaries and print each one
for entry in data:
    print(f"Name: {entry['name']}")
    print(f"Age: {entry['age']}")
    print(f"City: {entry['address']['city']}")
    print(f"State: {entry['address']['state']}")
    print()  # Print a newline for better readability
