class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object and calling methods
my_dog = Dog("Buddy", 3)
print(my_dog.description())
print(my_dog.speak("Woof Woof"))
