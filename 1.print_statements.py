def divide(a, b):
    print(f"divide called with a={a}, b={b}")
    if b == 0:
        print("Error: Division by zero")
        return None
    result = a / b
    print(f"Result of division: {result}")
    return result


divide(10, 2)
divide(10, 0)
