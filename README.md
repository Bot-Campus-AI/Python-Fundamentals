
---

# Python Dictionaries Tutorial

## Overview
This tutorial covers the basics of Python dictionaries, including how to create, access, modify, and manipulate them. Dictionaries are essential for storing and handling data in key-value pairs, and understanding them is crucial for any Python programmer.

## Table of Contents
1. [What are Dictionaries?](#what-are-dictionaries)
2. [Accessing Dictionary Elements](#accessing-dictionary-elements)
3. [Modifying Dictionary Elements](#modifying-dictionary-elements)
4. [Adding and Removing Elements](#adding-and-removing-elements)
5. [Dictionary Methods](#dictionary-methods)
6. [Iterating Over Dictionaries](#iterating-over-dictionaries)
7. [Nested Dictionaries](#nested-dictionaries)
8. [Practical Exercise](#practical-exercise)
9. [About BotCampus AI](#about-botcampus-ai)

## What are Dictionaries?
Dictionaries are collections of key-value pairs. Each key is unique and maps to a value. They are defined using curly braces `{}`.

```python
# Creating dictionaries
empty_dict = {}
person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

print(empty_dict)
print(person)
```

## Accessing Dictionary Elements
You can access values in a dictionary using their corresponding keys.

```python
person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

# Accessing values
name = person["name"]
age = person["age"]

print("Name:", name)
print("Age:", age)
```

## Modifying Dictionary Elements
You can modify values in a dictionary by assigning a new value to an existing key.

```python
person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

# Modifying values
person["age"] = 31
person["email"] = "mark_new@example.com"

print(person)
```

## Adding and Removing Elements
You can add new key-value pairs to a dictionary and remove existing ones.

```python
person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

# Adding a new key-value pair
person["address"] = "123 Main St"

# Removing a key-value pair
del person["email"]

print(person)
```

## Dictionary Methods
Dictionaries come with a variety of useful methods. Let's explore a few common ones.

```python
person = {
    "name": "Mark",
    "age": 30,
    "email": "mark@example.com"
}

# Using dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)
```

## Iterating Over Dictionaries
You can iterate over the keys, values, or key-value pairs in a dictionary using a `for` loop.

```python
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
```

## Nested Dictionaries
Dictionaries can also be nested, meaning you can have dictionaries within dictionaries.

```python
people = {
    "person1": {"name": "Mark", "age": 30},
    "person2": {"name": "Bob", "age": 25}
}

# Accessing nested dictionary elements
print(people["person1"]["name"])
print(people["person2"]["age"])
```

## Practical Exercise
Create a dictionary to store information about your favorite books, including title, author, and year of publication. Experiment with adding, modifying, and removing elements, and try iterating over the dictionary.

---
## About BotCampus AI

**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System

Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us

- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/Python-Fundamentals)

---

Thank you for embarking on your Python journey with BotCampus AI through this project. Happy coding!

---

© 2024 BotCampus AI. All rights reserved. 