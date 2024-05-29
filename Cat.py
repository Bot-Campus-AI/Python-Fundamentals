import Animal


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

# Creating objects of the derived classes
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.speak())
print(cat.speak())
