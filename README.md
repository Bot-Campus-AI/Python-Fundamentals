
---

# Python Sets Tutorial

## Overview
This tutorial covers the basics of Python sets, including how to create, add, remove, and manipulate them using various set operations. Sets are essential for handling collections of unique items and are a fundamental data structure in Python.

## Table of Contents
1. [What are Sets?](#what-are-sets)
2. [Adding and Removing Elements](#adding-and-removing-elements)
3. [Set Operations](#set-operations)
4. [Iterating Over Sets](#iterating-over-sets)
5. [Set Comprehensions](#set-comprehensions)
6. [Practical Exercise](#practical-exercise)

## What are Sets?
Sets are collections of unique items. Unlike lists or tuples, sets do not allow duplicate elements. They are defined using curly braces `{}` or the `set()` function.

```python
# Creating sets
empty_set = set()
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, 'Hello', 3.14, True}

print(empty_set)
print(numbers)
print(mixed_set)
```

## Adding and Removing Elements
You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods.

```python
numbers = {1, 2, 3, 4, 5}

# Adding an element
numbers.add(6)

# Removing an element
numbers.remove(3)

# Using discard to remove an element (doesn't raise an error if element is not found)
numbers.discard(10)

print(numbers)
```

## Set Operations
Sets support various operations like union, intersection, difference, and symmetric difference. These operations are useful for comparing and combining sets.

```python
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
union_set = set_a.union(set_b)

# Intersection
intersection_set = set_a.intersection(set_b)

# Difference
difference_set = set_a.difference(set_b)

# Symmetric Difference
sym_diff_set = set_a.symmetric_difference(set_b)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", sym_diff_set)
```

## Iterating Over Sets
You can iterate over the elements of a set using a `for` loop.

```python
numbers = {1, 2, 3, 4, 5}

# Iterating over a set
for num in numbers:
    print(num)
```

## Set Comprehensions
Set comprehensions provide a concise way to create sets. They consist of curly braces containing an expression followed by a `for` clause.

```python
# Creating a set of squares using a set comprehension
squares = {x**2 for x in range(6)}

print(squares)
```

## Practical Exercise
Create a set of your favorite fruits and try out different set operations: adding, removing, and performing union, intersection, and difference operations with another set.

---
