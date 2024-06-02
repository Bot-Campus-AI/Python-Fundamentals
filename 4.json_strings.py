import json

# JSON string
json_string = '{"name": "Luke", "age": 25, "address": {"city": "Los Angeles", "state": "CA"}}'

# Load JSON string into a Python dictionary
data = json.loads(json_string)
print(data)

# Convert Python dictionary back to a JSON string
json_string = json.dumps(data, indent=4)
print(json_string)
