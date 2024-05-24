# Nested if statements
number = 12

if number > 10:
    print("The number is greater than 10")
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is 10 or less")
