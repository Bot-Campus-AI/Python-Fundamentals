class Car:
    def __init__(self, make, model, year):
        self._make = make  # Private attribute
        self._model = model  # Private attribute
        self._year = year  # Private attribute

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
# Accessing private attributes directly (not recommended)
print(f"My car is a {my_car._year} {my_car._make} {my_car._model}")
