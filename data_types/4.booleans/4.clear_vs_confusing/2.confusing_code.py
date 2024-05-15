# Examples of confusing and improper use of booleans
is_member = "True"  # Incorrect: String instead of boolean
has_discount = "False"  # Incorrect: String instead of boolean

if is_member == "True" and has_discount == "False":  # Needs string comparison
    print("You are a member but don't have a discount.")
