import csv

# Open the CSV file
with open('example.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    # Iterate through the rows and print each row
    for row in csv_reader:
        print(row)
