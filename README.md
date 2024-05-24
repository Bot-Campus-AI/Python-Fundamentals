
---

# Python Loops Tutorial

## Overview
This tutorial covers the basics of using loops in Python, including how to use `for` and `while` loops to automate repetitive tasks. Understanding loops is essential for making your code more efficient and easier to manage.

## Table of Contents
1. [What are Loops?](#what-are-loops)
2. [For Loops](#for-loops)
3. [Iterating Over a String](#iterating-over-a-string)
4. [Using `range()` with For Loops](#using-range-with-for-loops)
5. [While Loops](#while-loops)
6. [Infinite Loops](#infinite-loops)
7. [Using `break` and `continue` Statements](#using-break-and-continue-statements)
8. [Nested Loops](#nested-loops)
9. [Loop Else Clause](#loop-else-clause)
10. [Practical Exercise](#practical-exercise)

## What are Loops?
Loops are used to execute a block of code repeatedly as long as a certain condition is met. They help in automating repetitive tasks, making your code more efficient and easier to manage.

## For Loops
A `for` loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.

```python
# Iterating over a list using a for loop
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

## Iterating Over a String
You can also use a `for` loop to iterate over the characters in a string.

```python
# Iterating over a string
message = "Hello, World!"

for char in message:
    print(char)
```

## Using `range()` with For Loops
The `range()` function generates a sequence of numbers, which is commonly used with `for` loops.

```python
# Using range() with a for loop
for i in range(5):
    print(i)
```

## While Loops
A `while` loop repeatedly executes a block of code as long as the specified condition is true.

```python
# Using a while loop
count = 0

while count < 5:
    print(count)
    count += 1
```

## Infinite Loops
Be careful with `while` loops! If the condition never becomes false, you can create an infinite loop that never stops running.

```python
# Example of an infinite loop (Commented out to avoid running indefinitely)
# while True:
#     print("This is an infinite loop!")
```

## Using `break` and `continue` Statements
The `break` statement exits the loop prematurely, while the `continue` statement skips the current iteration and continues with the next one.

```python
# Using break and continue in a loop
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

## Nested Loops
You can also nest loops, meaning you can have one loop inside another.

```python
# Nested for loops
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

## Loop Else Clause
Python allows an `else` clause with loops, which runs if the loop completes without encountering a `break` statement.

```python
# Using else with a loop
for i in range(5):
    print(i)
else:
    print("Loop completed without a break")
```

## Practical Exercise
Write a program that prints all the prime numbers between 1 and 20 using loops. Use `for` and `while` loops where appropriate.

---
