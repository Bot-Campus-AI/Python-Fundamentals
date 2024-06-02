import csv

# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Raj', '30', 'Delhi'],
    ['Pushpa', '25', 'Bangalore'],
    ['Priya', '35', 'Chennai']
]

# Open the CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write the data row by row
    for row in data:
        csv_writer.writerow(row)
