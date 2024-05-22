nested_tuple = (1, (2, 3), (4, (5, 6)))

# Accessing elements in a nested tuple
inner_tuple = nested_tuple[1]
deep_nested_element = nested_tuple[2][1][1]

print("Nested tuple:", nested_tuple)
print("Inner tuple:", inner_tuple)
print("Deep nested element:", deep_nested_element)
