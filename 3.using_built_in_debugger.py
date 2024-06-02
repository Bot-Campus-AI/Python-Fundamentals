import pdb


def divide(a, b):
    pdb.set_trace()  # Set a breakpoint
    if b == 0:
        return "Error: Division by zero"
    return a / b


print(divide(10, 2))
print(divide(10, 0))
