import csv

try:
    with open('nonexistent.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except FileNotFoundError:
    print("File not found. Please check the file path.")
except IOError:
    print("An error occurred while reading the file.")
