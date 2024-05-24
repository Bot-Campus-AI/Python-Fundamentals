class Dog:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

# Creating an object and accessing private attributes through methods
my_dog = Dog("Buddy", 3)
print(f"Original age: {my_dog.get_age()}")
my_dog.set_age(4)
print(f"New age: {my_dog.get_age()}")
