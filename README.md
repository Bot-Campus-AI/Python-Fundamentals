# Python Queue Operations Tutorial

## Overview
This tutorial covers the basics of implementing and using a queue in Python. A queue is a linear data structure that follows the First In, First Out (FIFO) principle. We'll explore how to perform basic queue operations such as enqueue, dequeue, peek, checking if the queue is empty, and getting the size of the queue.

## Table of Contents
1. [Creating a Queue](#creating-a-queue)
2. [Enqueue Operation](#enqueue-operation)
3. [Dequeue Operation](#dequeue-operation)
4. [Peek Operation](#peek-operation)
5. [IsEmpty Operation](#isempty-operation)
6. [Size Operation](#size-operation)

## Creating a Queue
A queue can be created using a Python list. Here's how you can initialize an empty queue.

```python
# Creating a queue
queue = []
```

## Enqueue Operation
The enqueue operation adds an element to the end of the queue. This can be done using the `append()` method.

```python
# Enqueue operation
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue after enqueue operations:", queue)
```
**Output:**
```
Queue after enqueue operations: [1, 2, 3]
```

## Dequeue Operation
The dequeue operation removes the front element from the queue. This can be done using the `pop(0)` method.

```python
# Dequeue operation
queue.pop(0)
print("Queue after dequeue operation:", queue)
```
**Output:**
```
Queue after dequeue operation: [2, 3]
```

## Peek Operation
The peek operation retrieves the front element of the queue without removing it. This can be done by accessing the first element of the list.

```python
# Peek operation
first_element = queue[0]
print("First element after dequeue operation:", first_element)
```
**Output:**
```
First element after dequeue operation: 2
```

## IsEmpty Operation
The `IsEmpty` operation checks if the queue is empty. This can be done by checking the length of the list.

```python
# IsEmpty operation
is_empty = len(queue) == 0
print("Is the queue empty?", is_empty)
```
**Output:**
```
Is the queue empty? False
```

## Size Operation
The size operation returns the current size of the queue. This can be done using the `len()` function.

```python
# Size operation
queue_size = len(queue)
print("Current queue size:", queue_size)
```
**Output:**
```
Current queue size: 2
```

---