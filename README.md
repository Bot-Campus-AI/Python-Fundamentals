
---

# Python OOP Tutorial: Encapsulation

## Overview
This tutorial covers the basics of encapsulation in Object-Oriented Programming (OOP) using Python. Encapsulation is the concept of bundling data and methods that operate on that data within one unit and restricting access to some of the object's components.

## Table of Contents
1. [What is Encapsulation?](#what-is-encapsulation)
2. [Defining a Simple Class with Public Attributes](#defining-a-simple-class-with-public-attributes)
3. [Converting Public Attributes to Private Attributes](#converting-public-attributes-to-private-attributes)
4. [Using Getter and Setter Methods](#using-getter-and-setter-methods)
5. [Using Property Decorators](#using-property-decorators)

## What is Encapsulation?
Encapsulation is one of the four fundamental OOP concepts. It allows us to hide the internal state of an object and require all interaction to be performed through the object's methods. This protects the integrity of the data and prevents external code from directly accessing and modifying it.

## Defining a Simple Class with Public Attributes
Let's start by defining a simple class with public attributes.

**File:** `1.public_attributes.py`
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")
```

## Converting Public Attributes to Private Attributes
Next, we'll convert the public attributes to private attributes by adding an underscore prefix.

**File:** `2.private_attributes.py`
```python
class Car:
    def __init__(self, make, model, year):
        self._make = make  # Private attribute
        self._model = model  # Private attribute
        self._year = year  # Private attribute

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
# Accessing private attributes directly (not recommended)
print(f"My car is a {my_car._year} {my_car._make} {my_car._model}")
```

## Using Getter and Setter Methods
To safely access and modify private attributes, we use getter and setter methods.

**File:** `3.getter_setter_methods.py`
```python
class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be a positive number")

# Creating an object of the Person class
person = Person("Alice", 30)
print(f"Person's age: {person.get_age()}")

# Using the setter method to update the age
person.set_age(35)
print(f"Updated age: {person.get_age()}")

# Attempting to set an invalid age
person.set_age(-5)
```

## Using Property Decorators
Python provides a more elegant way to define getters and setters using property decorators.

**File:** `4.property_decorators.py`
```python
class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year > 1885:
            self._year = year
        else:
            print("Invalid year for a car!")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(f"My car is a {my_car.year} {my_car._make} {my_car._model}")

# Using the property setter to update the year
my_car.year = 2021
print(f"Updated car year: {my_car.year}")

# Attempting to set an invalid year
my_car.year = 1800
```

---

## Summary
In this section, we covered the concept of encapsulation in Python. We defined a class with public attributes, converted them to private attributes, used getter and setter methods, and learned about property decorators. Encapsulation helps protect the integrity of data and provides a controlled way to access and modify it.

## Next Steps
In the next part of our series, we'll dive into polymorphism, another important OOP concept. Stay tuned!

---
