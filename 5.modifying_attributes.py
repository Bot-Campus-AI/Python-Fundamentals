class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        self.age = age

# Creating an object and modifying its attributes
my_dog = Dog("Buddy", 3)
print(f"Original age: {my_dog.age}")
my_dog.set_age(4)
print(f"New age: {my_dog.age}")
