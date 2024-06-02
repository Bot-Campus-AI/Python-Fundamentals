# Mastering Python: Working with CSV Files

## Overview
This tutorial covers how to work with CSV (Comma-Separated Values) files in Python. CSV files are a common format for storing tabular data, and being able to read from and write to CSV files is a valuable skill for any programmer. By the end of this tutorial, you'll understand how to handle CSV files using Python's built-in `csv` module.

## Table of Contents
1. [What is a CSV File?](#what-is-a-csv-file)
2. [Reading CSV Files](#reading-csv-files)
3. [Reading CSV Files with Headers](#reading-csv-files-with-headers)
4. [Writing to CSV Files](#writing-to-csv-files)
5. [Writing CSV Files with Headers](#writing-csv-files-with-headers)
6. [Handling File Exceptions](#handling-file-exceptions)
7. [About BotCampus AI](#about-botcampus-ai)

## What is a CSV File?
A CSV file is a plain text file that stores tabular data in a simple format: each row is a new line, and each column is separated by a comma. CSV files are widely used for data exchange between different applications.

## Reading CSV Files
Let's start by learning how to read data from a CSV file using Python's `csv` module.

**Code Example: Reading a CSV File**
```python
import csv

# Open the CSV file
with open('example.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Iterate through the rows and print each row
    for row in csv_reader:
        print(row)
```

## Reading CSV Files with Headers
If your CSV file has headers, you can use the `csv.DictReader` class to read the data into a dictionary.

**Code Example: Reading a CSV File with Headers**
```python
import csv

# Open the CSV file
with open('example_with_headers.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Iterate through the rows and print each row as a dictionary
    for row in csv_reader:
        print(row)
```

## Writing to CSV Files
Next, let's learn how to write data to a CSV file using the `csv` module.

**Code Example: Writing to a CSV File**
```python
import csv

# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

# Open the CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write the data row by row
    for row in data:
        csv_writer.writerow(row)
```

## Writing CSV Files with Headers
If you want to include headers in your CSV file, you can use the `csv.DictWriter` class.

**Code Example: Writing a CSV File with Headers**
```python
import csv

# Data to write
data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}
]

# Open the CSV file in write mode
with open('output_with_headers.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the data row by row
    for row in data:
        csv_writer.writerow(row)
```

## Handling File Exceptions
While working with CSV files, it's important to handle exceptions to manage errors like file not found or permission issues.

**Code Example: Handling File Exceptions**
```python
import csv

try:
    with open('nonexistent.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
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

Thank you for using this project to advance your Python skills with BotCampus AI. Enjoy your coding journey!

---

© 2024 BotCampus AI. All rights reserved.