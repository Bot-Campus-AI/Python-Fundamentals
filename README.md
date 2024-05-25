# Project: Polymorphism in Python

This project demonstrates how to calculate the area of different shapes using Object-Oriented Programming (OOP) principles in Python. It showcases polymorphism by defining a common interface for shapes and implementing it in different shape classes.

## File Structure

```
project/
│
├── shapes.py
├── triangle.py
└── main.py
```

## Files and Their Contents

### File: shapes.py

This file contains the base class `Shape` and two derived classes `Rectangle` and `Circle`.

```python
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
```

### File: triangle.py

This file contains the `Triangle` class that also inherits from `Shape` and implements the `area` method.

```python
from shapes import Shape

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```

### File: main.py

This file imports `Rectangle` and `Circle` from `shapes.py` and `Triangle` from `triangle.py`. It defines the `print_area` function and creates instances of `Rectangle`, `Circle`, and `Triangle`. It then calls `print_area` for each instance to demonstrate polymorphism.

```python
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
```

## How to Run

1. Save `shapes.py`, `triangle.py`, and `main.py` in the same directory (e.g., `project`).
2. Run `main.py` using your Python interpreter:
   ```sh
   python main.py
   ```

## Explanation

1. **shapes.py**: 
   - **Shape**: A base class with an abstract `area` method.
   - **Rectangle**: A derived class that implements the `area` method.
   - **Circle**: Another derived class that implements the `area` method.

2. **triangle.py**:
   - **Triangle**: A class that inherits from `Shape` and implements the `area` method.

3. **main.py**:
   - **Imports**: Imports `Rectangle` and `Circle` from `shapes.py` and `Triangle` from `triangle.py`.
   - **print_area Function**: A function that takes a shape object and prints its area.
   - **Instances**: Creates instances of `Rectangle`, `Circle`, and `Triangle`.
   - **Demonstration**: Calls `print_area` for each instance to demonstrate polymorphism.

By following this structure, you should be able to import the `Triangle` class without any import errors and successfully run the program to calculate and print the areas of different shapes.