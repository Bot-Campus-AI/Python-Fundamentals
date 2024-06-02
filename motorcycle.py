from vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, type_motorcycle):
        super().__init__(brand, model)
        self.type_motorcycle = type_motorcycle

    def wheelie(self):
        return "Doing a wheelie"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.type_motorcycle})"


# Example usage
motorcycle = Motorcycle("Yamaha", "MT-07", "Sport")
print(motorcycle)  # Outputs: Yamaha MT-07 (Sport)
motorcycle.start_engine()
print(motorcycle.wheelie())
motorcycle.stop_engine()
