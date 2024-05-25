
---

# Python Tuples Tutorial

## Overview
This tutorial covers the basics of Python tuples, including how to create, access, and manipulate them. Tuples are immutable collections that can store elements of different data types, making them a fundamental data structure in Python.

## Table of Contents
1. [What are Tuples?](#what-are-tuples)
2. [Accessing Tuple Elements](#accessing-tuple-elements)
3. [Immutability of Tuples](#immutability-of-tuples)
4. [Tuple Operations](#tuple-operations)
5. [Nested Tuples](#nested-tuples)
6. [Tuple Methods](#tuple-methods)
7. [Iterating Over Tuples](#iterating-over-tuples)
8. [Tuple Unpacking](#tuple-unpacking)
9. [Practical Exercise](#practical-exercise)
10. [About BotCampus AI](#about-botcampus-ai)

## What are Tuples?
Tuples are ordered collections of items that are immutable. They are defined using parentheses `()` and can store elements of different data types.

```python
# Creating tuples
empty_tuple = ()
numbers = (1, 2, 3, 4, 5)
mixed_tuple = (1, 'Hello', 3.14, True)

print(empty_tuple)
print(numbers)
print(mixed_tuple)
```

## Accessing Tuple Elements
You can access elements in a tuple using their index. Indexes start from 0.

```python
numbers = (1, 2, 3, 4, 5)

# Accessing elements
first_element = numbers[0]
third_element = numbers[2]
last_element = numbers[-1]

print("First element:", first_element)
print("Third element:", third_element)
print("Last element:", last_element)
```

## Immutability of Tuples
Tuples are immutable, meaning their elements cannot be changed after they are created.

```python
numbers = (1, 2, 3, 4, 5)

# Attempting to modify an element (This will raise an error)
# numbers[0] = 10

print(numbers)
```

## Tuple Operations
Although tuples are immutable, you can perform various operations on them, such as concatenation, repetition, and slicing.

```python
numbers = (1, 2, 3, 4, 5)
more_numbers = (6, 7, 8)

# Concatenation
concatenated_tuple = numbers + more_numbers

# Repetition
repeated_tuple = numbers * 2

# Slicing
sliced_tuple = numbers[1:4]

print("Concatenated tuple:", concatenated_tuple)
print("Repeated tuple:", repeated_tuple)
print("Sliced tuple:", sliced_tuple)
```

## Nested Tuples
Tuples can also be nested, meaning you can have tuples within tuples.

```python
nested_tuple = (1, (2, 3), (4, (5, 6)))

# Accessing elements in a nested tuple
inner_tuple = nested_tuple[1]
deep_nested_element = nested_tuple[2][1][1]

print("Nested tuple:", nested_tuple)
print("Inner tuple:", inner_tuple)
print("Deep nested element:", deep_nested_element)
```

## Tuple Methods
Tuples come with a few built-in methods, such as `count()` and `index()`.

```python
numbers = (1, 2, 3, 2, 4, 2, 5)

# Using count() to count occurrences of a value
count_of_twos = numbers.count(2)

# Using index() to find the index of a value
index_of_three = numbers.index(3)

print("Count of 2s:", count_of_twos)
print("Index of 3:", index_of_three)
```

## Iterating Over Tuples
You can iterate over the elements of a tuple using a `for` loop.

```python
numbers = (1, 2, 3, 4, 5)

# Iterating over a tuple
for num in numbers:
    print(num)
```

## Tuple Unpacking
Tuple unpacking allows you to assign the elements of a tuple to multiple variables in a single statement.

```python
person = ("Alice", 30, "Engineer")

# Unpacking tuple
name, age, profession = person

print("Name:", name)
print("Age:", age)
print("Profession:", profession)
```

## Practical Exercise
Create a tuple to store information about your favorite movies, including title, director, and year of release. Experiment with accessing, slicing, and unpacking the tuple.

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