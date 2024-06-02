# Open a file in read mode
with open('example.txt', 'r') as file:
    # Read the entire file content
    content = file.read()
    print(content)

    # Read a single line
    file.seek(0)  # Reset the file pointer to the beginning
    line = file.readline()
    print(line)

    # Read all lines into a list
    file.seek(0)  # Reset the file pointer to the beginning
    lines = file.readlines()
    print(lines)
