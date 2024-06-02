# Mastering Python: Working with JSON Files

## Overview
This tutorial covers how to work with JSON (JavaScript Object Notation) files in Python. JSON is a lightweight data interchange format that's easy for humans to read and write and easy for machines to parse and generate. By the end of this tutorial, you'll understand how to read from and write to JSON files using Python's built-in `json` module.

## Table of Contents
1. [What is JSON?](#what-is-json)
2. [Reading JSON Files](#reading-json-files)
3. [Accessing Data in a JSON Object](#accessing-data-in-a-json-object)
4. [Writing to JSON Files](#writing-to-json-files)
5. [Working with JSON Strings](#working-with-json-strings)
6. [Handling File Exceptions](#handling-file-exceptions)
7. [About BotCampus AI](#about-botcampus-ai)

## What is JSON?
JSON (JavaScript Object Notation) is a text-based format used for representing structured data. It is commonly used for data interchange between web applications and servers. JSON data is represented as key-value pairs, similar to Python dictionaries.

## Reading JSON Files
Let's start by learning how to read data from a JSON file using Python's `json` module.

**Code Example: Reading a JSON File**
```python
import json

# Open the JSON file and load the data
with open('example.json', 'r') as file:
    data = json.load(file)

# Print the loaded data
print(data)
```

## Accessing Data in a JSON Object
Once you've loaded the JSON data, you can access its values just like you would with a Python dictionary.

**Code Example: Accessing Data in a JSON Object**
```python

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

```

## Writing to JSON Files
Next, let's learn how to write data to a JSON file using the `json` module.

**Code Example: Writing to a JSON File**
```python
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
```

## Working with JSON Strings
You can also work with JSON data as strings, which is useful when dealing with web APIs or data that isn't stored in a file.

**Code Example: Working with JSON Strings**
```python
import json

# JSON string
json_string = '{"name": "Luke", "age": 25, "address": {"city": "Los Angeles", "state": "CA"}}'

# Load JSON string into a Python dictionary
data = json.loads(json_string)
print(data)

# Convert Python dictionary back to a JSON string
json_string = json.dumps(data, indent=4)
print(json_string)
```

## Handling File Exceptions
While working with JSON files, it's important to handle exceptions to manage errors like file not found or invalid JSON data.

**Code Example: Handling File Exceptions**
```python
import json

try:
    with open('nonexistent.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except json.JSONDecodeError:
    print("An error occurred while decoding the JSON data.")
```

## About BotCampus AI

**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System

Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us

- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/Python-Fundamentals)

---

We hope this project helps you enhance your Python skills with BotCampus AI. Enjoy your coding journey!

---

© 2024 BotCampus AI. All rights reserved.