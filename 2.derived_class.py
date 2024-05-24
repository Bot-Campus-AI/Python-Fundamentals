class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof Woof"

# Creating an object of the derived class
dog = Dog("Buddy")
print(dog.speak())
