import csv

# Open the CSV file
with open('example_with_headers.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    # Iterate through the rows and print each row as a dictionary
    for row in csv_reader:
        print(row)
