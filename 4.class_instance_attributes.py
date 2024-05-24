class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(f"{dog1.name} is a {dog1.species} and {dog2.name} is a {dog2.species}.")
