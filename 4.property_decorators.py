class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if year > 1885:
            self._year = year
        else:
            print("Invalid year for a car!")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(f"My car is a {my_car.year} {my_car._make} {my_car._model}")

# Using the property setter to update the year
my_car.year = 2021
print(f"Updated car year: {my_car.year}")

# Attempting to set an invalid year
my_car.year = 1800
