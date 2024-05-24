
---

# Python Conditional Statements Tutorial

## Overview
This tutorial covers the basics of Python conditional statements, including how to use `if`, `elif`, and `else` statements to control the flow of your program based on different conditions. Understanding conditional statements is essential for making decisions in your code.

## Table of Contents
1. [What are Conditional Statements?](#what-are-conditional-statements)
2. [Basic `if` Statement](#basic-if-statement)
3. [Using `else` Statement](#using-else-statement)
4. [Using `elif` Statement](#using-elif-statement)
5. [Nested Conditional Statements](#nested-conditional-statements)
6. [Logical Operators with Conditional Statements](#logical-operators-with-conditional-statements)
7. [Practical Exercise](#practical-exercise)

## What are Conditional Statements?
Conditional statements control the flow of your program based on certain conditions. They allow your program to make decisions and execute different code blocks accordingly.

## Basic `if` Statement
The `if` statement is used to test a condition. If the condition is true, the code block under the `if` statement is executed.

```python
# Simple if statement
number = 10

if number > 5:
    print("The number is greater than 5")
```

## Using `else` Statement
The `else` statement provides an alternative block of code that executes if the condition in the `if` statement is false.

```python
# if-else statement
number = 3

if number > 5:
    print("The number is greater than 5")
else:
    print("The number is not greater than 5")
```

## Using `elif` Statement
The `elif` (short for else if) statement allows you to check multiple conditions. If the first condition is false, it checks the next one, and so on.

```python
# if-elif-else statement
number = 7

if number > 10:
    print("The number is greater than 10")
elif number > 5:
    print("The number is greater than 5 but not greater than 10")
else:
    print("The number is 5 or less")
```

## Nested Conditional Statements
You can also nest conditional statements to check multiple conditions within the same block of code.

```python
# Nested if statements
number = 12

if number > 10:
    print("The number is greater than 10")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is 10 or less")
```

## Logical Operators with Conditional Statements
Logical operators like `and`, `or`, and `not` are often used with conditional statements to combine multiple conditions.

```python
# Using logical operators
number = 8

if number > 5 and number < 10:
    print("The number is between 5 and 10")

if number < 5 or number > 10:
    print("The number is either less than 5 or greater than 10")

if not (number > 10):
    print("The number is not greater than 10")
```

## Practical Exercise
Write a program that takes an input number from the user and checks if the number is positive, negative, or zero. Use `if`, `elif`, and `else` statements to handle the conditions.

---
