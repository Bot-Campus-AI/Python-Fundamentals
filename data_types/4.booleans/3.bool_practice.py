# Practical exercises and tasks for booleans
def is_adult(age):
    return age >= 18

def is_eligible_to_vote(age):
    return age >= 18 and age < 120  # Assuming a realistic voting age range

print(is_adult(20))
print(is_eligible_to_vote(20))
