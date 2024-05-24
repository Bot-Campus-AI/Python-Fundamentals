
---

# Python OOP Tutorial: Classes and Objects

## Overview
This tutorial covers the basics of Object-Oriented Programming (OOP) in Python, focusing on classes and objects. By the end of this tutorial, you will understand how to define classes, create objects, and use them effectively.

## Table of Contents
1. [What are Classes and Objects?](#what-are-classes-and-objects)
2. [Defining a Basic Class](#defining-a-basic-class)
3. [Adding Attributes](#adding-attributes)
4. [Adding Methods](#adding-methods)
5. [Class Attributes vs. Instance Attributes](#class-attributes-vs-instance-attributes)
6. [Modifying Attributes](#modifying-attributes)
7. [Encapsulation](#encapsulation)

## What are Classes and Objects?
Classes are blueprints for creating objects. An object is an instance of a class. Classes encapsulate data for the object and methods to manipulate that data.

## Defining a Basic Class
Let's start by defining a simple class.

```python
class Dog:
    pass

# Creating an object
my_dog = Dog()
print(my_dog)
```

## Adding Attributes
Next, we'll add some attributes to our class. Attributes are variables that belong to an object.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object with attributes
my_dog = Dog("Buddy", 3)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age} years old.")
```

## Adding Methods
Methods are functions that belong to an object. Let's add some methods to our class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object and calling methods
my_dog = Dog("Buddy", 3)
print(my_dog.description())
print(my_dog.speak("Woof Woof"))
```

## Class Attributes vs. Instance Attributes
Let's understand the difference between class attributes and instance attributes.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"{dog1.name} is a {dog1.species} and {dog2.name} is a {dog2.species}.")
```

## Modifying Attributes
Let's see how we can modify the attributes of an object.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

# Creating an object and modifying its attributes
my_dog = Dog("Buddy", 3)
print(f"Original age: {my_dog.age}")
my_dog.set_age(4)
print(f"New age: {my_dog.age}")
```

## Encapsulation
Encapsulation is the concept of restricting access to certain components of an object and making them private. Let's see how to do that.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

# Creating an object and accessing private attributes through methods
my_dog = Dog("Buddy", 3)
print(f"Original age: {my_dog.get_age()}")
my_dog.set_age(4)
print(f"New age: {my_dog.get_age()}")
```

---
