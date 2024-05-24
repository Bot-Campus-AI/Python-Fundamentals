def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()

# Trying to access local_var outside the function will raise an error
# print(local_var)  # Uncommenting this line will raise a NameError
