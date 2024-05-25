from shapes import Rectangle, Circle
from triangle import Triangle


def print_area(shape):
    print(f"The area is: {shape.area()}")


# Creating instances of Rectangle, Circle, and Triangle
rectangle = Rectangle(3, 4)
circle = Circle(5)
triangle = Triangle(4, 5)

# Using the function with different objects
print_area(rectangle)  # Output: The area is: 12
print_area(circle)     # Output: The area is: 78.5
print_area(triangle)   # Output: The area is: 10
