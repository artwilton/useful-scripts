import csv

csv_file_path = "/Users/arthur/Desktop/csv_test.csv"
row_split_amount = 10000

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    column_headers = []
  
    # loop to iterate thorugh the rows of csv
    for row in csv_reader:
  
        # adding the first row
        column_headers.append(row)
  
        # breaking the loop after the
        # first iteration itself
        break

    print(column_headers)