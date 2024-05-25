
---

# Python Practical Project: Building a Simple Contact Book

## Overview
This project demonstrates how to combine different data types in Python by building a simple contact book application. You'll learn how to create, view, and search for contacts using strings, integers, and booleans.

## Table of Contents
1. [Setting Up the Project](#setting-up-the-project)
2. [Adding a Contact](#adding-a-contact)
3. [Viewing Contacts](#viewing-contacts)
4. [Searching for a Contact](#searching-for-a-contact)
5. [Main Program Loop](#main-program-loop)
6. [Practical Exercise](#practical-exercise)
7. [About BotCampus AI](#about-botcampus-ai)

## Setting Up the Project
First, set up your project structure and create a list to store your contacts.

```python
# List to store contacts
contacts = []
```

## Adding a Contact
Create a function to add a contact to the contact book. This function will prompt the user to input the contact's name, phone number, and email address.

```python
def add_contact():
    name = input("Enter contact name: ")
    phone = int(input("Enter contact phone number: "))
    email = input("Enter contact email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

# Adding a contact for demonstration
add_contact()
print(contacts)
```

## Viewing Contacts
Create a function to view all contacts stored in the contact book.

```python
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

# Viewing contacts for demonstration
view_contacts()
```

## Searching for a Contact
Create a function to search for a contact by name.

```python
def search_contact(name):
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.")

# Searching for a contact for demonstration
search_contact("Alice")
```

## Main Program Loop
Put everything together in a main program loop that allows the user to choose between adding a contact, viewing contacts, and searching for a contact.

```python
def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to search: ")
            search_contact(name)
        elif choice == '4':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the main program loop
main()
```

## Practical Exercise
Extend the contact book application by adding more features, such as deleting a contact or updating contact information. Experiment with different data types and see how they can be used together in a real-world application.

---
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
