# Mastering Python: File Input/Output (I/O) Operations

## Overview
This tutorial covers the basics of file input/output (I/O) operations in Python. File I/O is crucial for reading from and writing to files, enabling you to manage and manipulate data effectively. By the end of this tutorial, you'll understand how to perform basic file I/O operations in Python.

## Table of Contents
1. [What is File I/O?](#what-is-file-io)
2. [Opening and Closing Files](#opening-and-closing-files)
3. [Writing to a File](#writing-to-a-file)
4. [Reading from a File](#reading-from-a-file)
5. [Appending to a File](#appending-to-a-file)
6. [Working with Binary Files](#working-with-binary-files)
7. [Handling File Exceptions](#handling-file-exceptions)
8. [About BotCampus AI](#about-botcampus-ai)

## What is File I/O?
File I/O operations refer to the process of reading data from and writing data to files. This is essential for tasks such as saving program output, processing data from files, and managing application configurations.

## Opening and Closing Files
Let's start by learning how to open and close files in Python. The `open` function is used to open a file, and the `close` method is used to close it.

**Code Example: Opening and Closing Files**
```python
# Open a file
file = open('example.txt', 'w')

# Perform file operations (write data)
file.write("Hello, World!")

# Close the file
file.close()
```

## Writing to a File
To write data to a file, you can use the `write` method. Let's see how to write some text to a file.

**Code Example: Writing to a File**
```python
# Open a file in write mode
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("Welcome to Python file I/O operations.")
```

## Reading from a File
Reading data from a file can be done using methods like `read`, `readline`, and `readlines`. Let's explore each of these methods.

**Code Example: Reading from a File**
```python
# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read the entire file content
    content = file.read()
    print(content)

    # Read a single line
    file.seek(0)  # Reset the file pointer to the beginning
    line = file.readline()
    print(line)

    # Read all lines into a list
    file.seek(0)  # Reset the file pointer to the beginning
    lines = file.readlines()
    print(lines)
```

## Appending to a File
If you want to add data to an existing file without overwriting it, you can open the file in append mode.

**Code Example: Appending to a File**
```python
# Open a file in append mode
with open('example.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")
```

## Working with Binary Files
Besides text files, you can also work with binary files. Let's see how to read from and write to a binary file.

**Code Example: Working with Binary Files**
```python
# Writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

# Reading from a binary file
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
```

## Handling File Exceptions
While working with files, it's important to handle exceptions to manage errors like missing files or permission issues.

**Code Example: Handling File Exceptions**
```python
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found. Please check the file path.")
except IOError:
    print("An error occurred while reading the file.")
```

## About BotCampus AI

**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System

Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us

- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/Python-Fundamentals)

---

We appreciate you starting your Python journey with BotCampus AI through this project. Enjoy coding!

---

© 2024 BotCampus AI. All rights reserved.