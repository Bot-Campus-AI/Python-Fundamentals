# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound"


# Derived Class Using super():
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class's __init__ method
        self.breed = breed

    def speak(self):
        return f"{self.name} the {self.breed} says Woof Woof"


# Using the Derived Class:
# Creating an object of the derived class
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Output: Buddy the Golden Retriever says Woof Woof




