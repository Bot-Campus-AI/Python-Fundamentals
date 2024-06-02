import csv

# Data to write
data = [
    {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
    {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}
]

# Open the CSV file in write mode
with open('output_with_headers.csv', mode='w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    csv_writer.writeheader()

    # Write the data row by row
    for row in data:
        csv_writer.writerow(row)
