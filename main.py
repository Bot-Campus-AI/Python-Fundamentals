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
