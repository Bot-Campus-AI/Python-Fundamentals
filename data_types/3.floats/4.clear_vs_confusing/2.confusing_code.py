# Examples of confusing and improper use of floats
price = "19.99"  # Incorrect: String instead of float
quantity = "3"  # Incorrect: String instead of integer
total_cost = float(price) * int(quantity)  # Needs conversion
print("Total cost: $" + str(total_cost))  # Needs conversion
