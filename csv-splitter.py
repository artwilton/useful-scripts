import csv

csv_file_path = "/Users/arthur/Desktop/csv_test.csv"
row_split_amount = 10000

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    column_headers = []
    line_count = 0
  
    for row in csv_reader:

        if line_count == 0:
            column_headers = row
            line_count += 1
  
        line_count += 1

    print(column_headers)