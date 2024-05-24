
---

# Python Functions Tutorial

## Overview
This tutorial covers the basics of Python functions, including how to define, use, and leverage various features of functions to modularize and organize your code. By the end of this tutorial, you will have a solid understanding of how to work with functions in Python.

## Table of Contents
1. [What are Functions?](#what-are-functions)
2. [Defining a Function](#defining-a-function)
3. [Function Parameters](#function-parameters)
4. [Returning Values](#returning-values)
5. [Default Parameters](#default-parameters)
6. [Keyword Arguments](#keyword-arguments)
7. [Variable-Length Arguments](#variable-length-arguments)
8. [Scope and Lifetime of Variables](#scope-and-lifetime-of-variables)
9. [Practical Exercise](#practical-exercise)

## What are Functions?
Functions are blocks of code that perform a specific task. They can take inputs, called parameters, and return an output. Functions help you organize your code into reusable pieces.

## Defining a Function
To define a function in Python, use the `def` keyword followed by the function name and parentheses.

```python
# Defining a simple function
def greet():
    print("Hello, World!")

# Calling the function
greet()
```

## Function Parameters
Functions can take parameters, which allow you to pass data into the function.

```python
# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Alice")
```

## Returning Values
Functions can return values using the `return` keyword. This allows you to get a result back from the function.

```python
# Function with a return value
def add(a, b):
    return a + b

# Calling the function and storing the result
result = add(3, 5)
print("Result:", result)
```

## Default Parameters
Functions can have default parameters, which provide default values if no arguments are passed.

```python
# Function with default parameters
def greet(name="World"):
    print(f"Hello, {name}!")

# Calling the function with and without an argument
greet()
greet("Alice")
```

## Keyword Arguments
Functions can be called using keyword arguments, which allow you to specify arguments by name.

```python
# Function with multiple parameters
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

# Calling the function with keyword arguments
describe_person(name="Alice", age=30, city="New York")
```

## Variable-Length Arguments
Functions can accept a variable number of arguments using `*args` and `**kwargs`.

```python
# Function with *args
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Calling the function with multiple arguments
print("Sum:", add(1, 2, 3, 4, 5))

# Function with **kwargs
def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

# Calling the function with keyword arguments
describe_person(name="Alice", age=30, city="New York")
```

## Scope and Lifetime of Variables
Variables defined inside a function are local to that function and cannot be accessed outside. This is known as the variable's scope.

```python
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()

# Trying to access local_var outside the function will raise an error
# print(local_var)  # Uncommenting this line will raise a NameError
```

## Practical Exercise
Write a function that takes a list of numbers and returns the average. Test your function with different lists of numbers.

---
