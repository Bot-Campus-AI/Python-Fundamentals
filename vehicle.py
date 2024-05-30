class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return "Engine started"

    def stop_engine(self):
        return "Engine stopped"

    def __str__(self):
        return f"{self.brand} {self.model}"


# Example usage
vehicle = Vehicle("Generic Brand", "Generic Model")
print(vehicle)
print(vehicle.start_engine())
print(vehicle.stop_engine())
