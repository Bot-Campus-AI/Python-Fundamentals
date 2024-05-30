from vehicle import Vehicle


class Bicycle(Vehicle):
    def __init__(self, brand, model, gear_count):
        super().__init__(brand, model)
        self.gear_count = gear_count

    def ring_bell(self):
        return "Ring ring!"

    def __str__(self):
        return f"{self.brand} {self.model} with {self.gear_count} gears"


# Example usage
bicycle = Bicycle("Giant", "Escape 3", 21)
print(bicycle)
print(bicycle.ring_bell())
