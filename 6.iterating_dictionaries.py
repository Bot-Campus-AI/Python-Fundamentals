person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

# Iterating over keys
for key in person:
    print(key, ":", person[key])

# Iterating over values
for value in person.values():
    print(value)

# Iterating over key-value pairs
for key, value in person.items():
    print(key, ":", value)
