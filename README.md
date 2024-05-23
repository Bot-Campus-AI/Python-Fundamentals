# Python Stack Operations Tutorial

## Overview
This tutorial covers the basics of implementing and using a stack in Python. A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. We'll explore how to perform basic stack operations such as push, pop, peek, checking if the stack is empty, and getting the size of the stack.

## Table of Contents
1. [Creating a Stack](#creating-a-stack)
2. [Push Operation](#push-operation)
3. [Pop Operation](#pop-operation)
4. [Peek Operation](#peek-operation)
5. [IsEmpty Operation](#isempty-operation)
6. [Size Operation](#size-operation)

## Creating a Stack
A stack can be created using a Python list. Here's how you can initialize an empty stack.

```python
# Creating a stack
stack = []
```

## Push Operation
The push operation adds an element to the top of the stack. This can be done using the `append()` method.

```python
# Push operation
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack after push operations:", stack)
```
**Output:**
```
Stack after push operations: [1, 2, 3]
```

## Pop Operation
The pop operation removes the top element from the stack. This can be done using the `pop()` method.

```python
# Pop operation
stack.pop()
print("Stack after pop operation:", stack)
```
**Output:**
```
Stack after pop operation: [1, 2]
```

## Peek Operation
The peek operation retrieves the top element of the stack without removing it. This can be done by accessing the last element of the list.

```python
# Peek operation
top_element = stack[-1]
print("Top element after pop operation:", top_element)
```
**Output:**
```
Top element after pop operation: 2
```

## IsEmpty Operation
The `IsEmpty` operation checks if the stack is empty. This can be done by checking the length of the list.

```python
# IsEmpty operation
is_empty = len(stack) == 0
print("Is the stack empty?", is_empty)
```
**Output:**
```
Is the stack empty? False
```

## Size Operation
The size operation returns the current size of the stack. This can be done using the `len()` function.

```python
# Size operation
stack_size = len(stack)
print("Current stack size:", stack_size)
```
**Output:**
```
Current stack size: 2
```

---

Feel free to use this README file for your GitHub repository. If you need further adjustments or additions, let me know!