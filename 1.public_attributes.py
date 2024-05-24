class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)
print(f"My car is a {my_car.year} {my_car.make} {my_car.model}")
