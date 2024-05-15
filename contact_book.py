# contact_book.py

# List to store contacts
contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = int(input("Enter contact phone number: "))
    email = input("Enter contact email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def search_contact(name):
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found.")

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

if __name__ == "__main__":
    main()
