
---

# Python OOP Tutorial: Inheritance

## Overview
This tutorial covers the basics of inheritance in Object-Oriented Programming (OOP) using Python. Inheritance allows us to create new classes from existing classes, helping in reusing code and creating a class hierarchy.

## Table of Contents
1. [What is Inheritance?](#what-is-inheritance)
2. [Defining a Base Class](#defining-a-base-class)
3. [Creating a Derived Class](#creating-a-derived-class)
4. [Inheriting Attributes and Methods](#inheriting-attributes-and-methods)
5. [Extending Functionality](#extending-functionality)
6. [Understanding `super()`](#understanding-super)
7. [About BotCampus AI](#about-botcampus-ai)

## What is Inheritance?
Inheritance is a way to form new classes using classes that have already been defined. The new class, known as the derived class, inherits attributes and methods from the existing class, called the base class.

## Defining a Base Class
Let's start by defining a simple base class.

**File:** `1.base_class.py`
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Creating an object of the base class
animal = Animal("Generic Animal")
print(f"Animal name: {animal.name}")
```

## Creating a Derived Class
Now, let's create a derived class that inherits from the base class.

**File:** `2.derived_class.py`
```python
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof Woof"

# Creating an object of the derived class
dog = Dog("Buddy")
print(dog.speak())
```

## Inheriting Attributes and Methods
The derived class inherits all attributes and methods from the base class.

**File:** `3.inherit_attributes_methods.py`
```python
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())
```

## Extending Functionality
Let's create a derived class that extends the functionality of the base class.

**File:** `4.extend_functionality.py`
```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof Woof"

# Creating an object of the derived class
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())
```

## Understanding `super()`
The `super()` function allows you to call methods from a parent class, which is useful for extending or modifying inherited methods.

**File:** `5.understanding_super.py`
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__ method
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof Woof"

# Creating an object of the derived class
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy the Golden Retriever says Woof Woof
```

---

## Summary
In this section, we covered the basics of inheritance in Python. We defined a base class, created derived classes, inherited attributes and methods, extended functionality, and understood the use of the `super()` function. Inheritance helps us write more efficient and maintainable code.

## Next Steps
In the next part of our series, we'll dive into encapsulation, another important OOP concept. Stay tuned!

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