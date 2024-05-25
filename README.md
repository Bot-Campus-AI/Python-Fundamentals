# Python OOP Tutorial: Composition

## Overview
This tutorial covers the concept of composition in Object-Oriented Programming (OOP) using Python. Composition allows us to build complex objects by combining simpler ones, promoting code reuse and flexibility.

## Table of Contents
1. [What is Composition?](#what-is-composition)
2. [Defining Simple Classes](#defining-simple-classes)
3. [Defining a Complex Class Using Composition](#defining-a-complex-class-using-composition)
4. [Using the Complex Class](#using-the-complex-class)
5. [Summary](#summary)
6. [Next Steps](#next-steps)
7. [How to Run](#how-to-run)
8. [Explanation](#explanation)
9. [About BotCampus AI](#about-botcampus-ai)

## What is Composition?
Composition is a design principle where one class contains an object of another class to achieve code reuse and flexibility. It allows us to build complex objects by combining simpler ones.

## Defining Simple Classes
Let's start by defining some simple classes that we will use for composition.

**File:** `engine.py`
```python
class Engine:
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"
```

**File:** `transmission.py`
```python
class Transmission:
    def engage(self):
        return "Transmission engaged"

    def disengage(self):
        return "Transmission disengaged"
```

## Defining a Complex Class Using Composition
Now, let's define a complex class `Car` that uses `Engine` and `Transmission` objects through composition.

**File:** `car.py`
```python
from engine import Engine
from transmission import Transmission

class Car:
    def __init__(self):
        self.engine = Engine()
        self.transmission = Transmission()

    def start(self):
        return f"{self.engine.start()} and {self.transmission.engage()}"

    def stop(self):
        return f"{self.transmission.disengage()} and {self.engine.stop()}"
```

## Using the Complex Class
Let's create an instance of the `Car` class and use its methods.

**File:** `main.py`
```python
from car import Car

# Creating an instance of Car
my_car = Car()

# Using the start and stop methods
print(my_car.start())  # Output: Engine started and Transmission engaged
print(my_car.stop())   # Output: Transmission disengaged and Engine stopped
```

## Summary
In this section, we covered the concept of composition in Python. We defined simple classes `Engine` and `Transmission`, and then created a complex class `Car` that uses these objects through composition. Composition allows us to build complex objects by combining simpler ones, promoting code reuse and flexibility.

## Next Steps
In the next part of our series, we'll explore another important OOP concept: aggregation. Stay tuned!

## How to Run
1. Save `engine.py`, `transmission.py`, `car.py`, and `main.py` in the same directory (e.g., `project`).
2. Run `main.py` using your Python interpreter:
   ```sh
   python main.py
   ```

## Explanation
1. **engine.py**:
   - **Engine**: A class with `start` and `stop` methods.

2. **transmission.py**:
   - **Transmission**: A class with `engage` and `disengage` methods.

3. **car.py**:
   - **Car**: A class that uses `Engine` and `Transmission` objects through composition.
   - **Methods**: The `start` method starts the engine and engages the transmission, while the `stop` method disengages the transmission and stops the engine.

4. **main.py**:
   - **Imports**: Imports the `Car` class from `car.py`.
   - **Instance**: Creates an instance of the `Car` class and demonstrates the use of composition by calling the `start` and `stop` methods.

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