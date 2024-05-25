class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Creating instances of Rectangle and Circle
rectangle = Rectangle(3, 4)
circle = Circle(5)

print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 12
print(f"Circle area: {circle.area()}")        # Output: Circle area: 78.5
