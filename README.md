
---

# Python Numbers Tutorial: Integers

## Overview
This tutorial covers the basics of Python integers, including how to define, manipulate, and perform arithmetic operations with them. Integers are a fundamental data type in Python, essential for various programming tasks. By the end of this tutorial, you will understand how to work with integers effectively in Python.

## Table of Contents
1. [Defining Integers](#defining-integers)
2. [Basic Arithmetic Operations](#basic-arithmetic-operations)
3. [Integer Division and Floor Division](#integer-division-and-floor-division)
4. [Working with Large Integers](#working-with-large-integers)
5. [Type Conversion](#type-conversion)
6. [Practical Exercise](#practical-exercise)

## Defining Integers
In Python, integers are whole numbers without a fractional component. They can be positive, negative, or zero.

```python
positive_int = 42
negative_int = -42
zero = 0

print(positive_int)
print(negative_int)
print(zero)
```

## Basic Arithmetic Operations
You can perform standard arithmetic operations with integers in Python, such as addition, subtraction, multiplication, and division.

```python
a = 10
b = 3

# Addition
addition = a + b

# Subtraction
subtraction = a - b

# Multiplication
multiplication = a * b

# Division
division = a / b  # This returns a float

# Floor Division
floor_division = a // b  # This returns an integer

# Modulus
modulus = a % b

# Exponentiation
exponentiation = a ** b

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
```

## Integer Division and Floor Division
Regular division using `/` returns a float, while floor division using `//` returns an integer by discarding the fractional part.

```python
# Regular division
regular_div = 10 / 3  # Returns 3.333...

# Floor division
floor_div = 10 // 3  # Returns 3

print("Regular Division:", regular_div)
print("Floor Division:", floor_div)
```

## Working with Large Integers
Python supports arbitrarily large integers, allowing you to work with extremely large numbers without any issues.

```python
large_int = 123456789012345678901234567890
print("Large Integer:", large_int)
```

## Type Conversion
You can convert other data types to integers using the `int()` function. For example, converting a string or a float to an integer.

```python
# Convert string to integer
num_str = "100"
num_int = int(num_str)

# Convert float to integer
num_float = 12.34
num_int_from_float = int(num_float)

print("String to Integer:", num_int)
print("Float to Integer:", num_int_from_float)
```

## Practical Exercise
Create integer variables and perform various arithmetic operations on them. Try converting strings and floats to integers and see the results.

---