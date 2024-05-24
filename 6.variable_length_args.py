# "Functions can accept a variable number of arguments using *args and **kwargs."
# Function with *args
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Calling the function with multiple arguments
print("Sum:", add(1, 2, 3, 4, 5))


# Function with **kwargs
def describe_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
        

# Calling the function with keyword arguments
describe_person(name="Alice", age=30, city="New York")
