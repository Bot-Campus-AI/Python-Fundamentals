# Python OOP Tutorial: Abstract Classes and Interfaces

## Overview
This tutorial covers the basics of abstract classes and interfaces in Object-Oriented Programming (OOP) using Python. Abstract classes and interfaces help us create a blueprint for other classes, enforcing a certain structure and behavior.

## Table of Contents
1. [What are Interfaces?](#what-are-interfaces)
2. [Implementing an Interface](#implementing-an-interface)
3. [What are Abstract Base Classes?](#what-are-abstract-base-classes)
4. [Creating Derived Classes](#creating-derived-classes)
5. [Using the Abstract Base Class and Derived Classes](#using-the-abstract-base-class-and-derived-classes)
6. [Complete Example with Files](#complete-example-with-files)
7. [How to Run](#how-to-run)
8. [Explanation](#explanation)

## What are Interfaces?
An interface is a class that contains only abstract methods. It defines a set of methods that the implementing class must provide. In Python, we can use abstract classes to create interfaces.

### Defining an Interface
Let's define an interface using the `abc` module.

**File:** `1.interface.py`
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
```

### Implementing the Interface
Now, let's create a class that implements the `PaymentProcessor` interface.

**File:** `2.implement_interface.py`
```python
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

# Creating an instance of CreditCardProcessor
processor = CreditCardProcessor()

# Using the process_payment method
print(processor.process_payment(100))  # Output: Processing credit card payment of $100
```

## What are Abstract Base Classes?
An abstract base class (ABC) is a class that cannot be instantiated and is typically used as a base class. It can define abstract methods that must be implemented by derived classes. Unlike interfaces, abstract base classes can also have concrete methods.

### Defining an Abstract Base Class
Let's start by defining an abstract base class using the `abc` module.

**File:** `3.abstract_base_class.py`
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    def describe_role(self):
        return "This is an employee"
```

## Creating Derived Classes
Now, let's create derived classes that implement the abstract methods and also use the concrete method from the abstract base class.

**File:** `4.derived_classes.py`
```python
class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
```

## Using the Abstract Base Class and Derived Classes
Let's see how we can use the abstract base class and the derived classes.

**File:** `5.use_abstract_base_class.py`
```python
def print_employee_info(employee):
    print(employee.describe_role())
    print(f"Salary: ${employee.calculate_salary()}")

# Creating instances of FullTimeEmployee and PartTimeEmployee
full_time_employee = FullTimeEmployee("Alice", 5000)
part_time_employee = PartTimeEmployee("Bob", 20, 100)

# Using the function with different objects
print_employee_info(full_time_employee)
print_employee_info(part_time_employee)
```

## Complete Example with Files

### File Structure
```
project/
│
├── payment_processor.py
├── employee.py
└── main.py
```

### File: payment_processor.py
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"
```

### File: employee.py
```python
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    def describe_role(self):
        return "This is an employee"

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
```

### File: main.py
```python
from payment_processor import CreditCardProcessor
from employee import FullTimeEmployee, PartTimeEmployee

def print_employee_info(employee):
    print(employee.describe_role())
    print(f"Salary: ${employee.calculate_salary()}")

# Creating instances of FullTimeEmployee and PartTimeEmployee
full_time_employee = FullTimeEmployee("Alice", 5000)
part_time_employee = PartTimeEmployee("Bob", 20, 100)

# Using the function with different objects
print_employee_info(full_time_employee)  # Output: This is an employee. Salary: $5000
print_employee_info(part_time_employee)  # Output: This is an employee. Salary: $2000

# Using the CreditCardProcessor
processor = CreditCardProcessor()
print(processor.process_payment(100))  # Output: Processing credit card payment of $100
```

## How to Run
1. Save `payment_processor.py`, `employee.py`, and `main.py` in the same directory (e.g., `project`).
2. Run `main.py` using your Python interpreter:
   ```sh
   python main.py
   ```

## Explanation
1. **payment_processor.py**:
   - **PaymentProcessor**: An interface with an abstract method `process_payment`.
   - **CreditCardProcessor**: A class that implements `PaymentProcessor`.

2. **employee.py**:
   - **Employee**: An abstract base class with an abstract method `calculate_salary` and a concrete method `describe_role`.
   - **FullTimeEmployee**: A derived class that implements the `calculate_salary` method.
   - **PartTimeEmployee**: Another derived class that implements the `calculate_salary` method.

3. **main.py**:
   - **Imports**: Imports `CreditCardProcessor` from `payment_processor.py` and `FullTimeEmployee`, `PartTimeEmployee` from `employee.py`.
   - **print_employee_info Function**: A function that takes an employee object and prints its role and salary.
   - **Instances**: Creates instances of `FullTimeEmployee` and `PartTimeEmployee`, and demonstrates polymorphism.
   - **Processor Instance**: Creates an instance of `CreditCardProcessor` and demonstrates interface implementation.

By following this structure, you can implement abstract classes and interfaces in Python, and demonstrate their usage with clear examples, differentiating between interfaces and abstract base classes effectively.

---
