import csv

# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

# Open the CSV file in write mode
with open('output.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write the data row by row
    for row in data:
        csv_writer.writerow(row)
