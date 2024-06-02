# Writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03\x04')

# Reading from a binary file
with open('example.bin', 'rb') as file:
    binary_content = file.read()
    print(binary_content)
