# Examples of confusing and improper use of integers
age = '25'  # Incorrect: String instead of integer
years_to_retirement = 65 - int(age)  # Needs conversion
print("Years to retirement: " + str(years_to_retirement))  # Needs conversion
