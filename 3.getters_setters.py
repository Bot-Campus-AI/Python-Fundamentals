class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute
        self._age = age    # Private attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be a positive number")

# Creating an object of the Person class
person = Person("Alice", 30)
print(f"Person's age: {person.get_age()}")

# Using the setter method to update the age
person.set_age(35)
print(f"Updated age: {person.get_age()}")

# Attempting to set an invalid age
person.set_age(-5)
