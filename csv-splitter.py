import csv

csv_file_path = "/Users/arthur/Desktop/csv_test.csv"
row_split_amount = 10000

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        print(row)