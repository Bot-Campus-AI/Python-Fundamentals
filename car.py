from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def play_radio(self):
        return "Playing radio"

    def __str__(self):
        return f"{self.brand} {self.model} with {self.num_doors} doors"


# Example usage
car = Car("Toyota", "Corolla", 4)
print(car)
print(car.start_engine())
print(car.play_radio())
print(car.stop_engine())
