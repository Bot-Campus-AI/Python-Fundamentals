# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "This animal makes a sound"


# Derived Class
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof Woof"


# Using Derived Class
# Creating an object of the derived class
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy says Woof Woof


# Another Derived Class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"


# Multiple Derived Classes
# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())   # Output: Buddy says Woof, Woof
print(cat.speak())   # Output: Whiskers says Meow

