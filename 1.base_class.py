class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Creating an object of the base class
animal = Animal("Generic Animal")
print(f"Animal name: {animal.name}")
