import json

# Data to write to a JSON file
data = {
    'name': 'Mark',
    'age': 30,
    'address': {
        'city': 'New York',
        'state': 'NY'
    }
}

# Open the JSON file in write mode and dump the data
with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)
