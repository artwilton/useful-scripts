import csv

csv_file_path = "/Users/arthur/Desktop/csv_test.csv"
split_threshold = int(input('Enter how many rows per CSV file you would like: '))

def grabColumnHeaders(row):
    column_headers = []
    for key in row.keys():
        column_headers.append(key)
    
    return column_headers

def writeNewCsv(csv_file, column_headers, split_number):

    writer = csv.DictWriter(csv_file, fieldnames=column_headers)
    writer.writeheader()

    return writer

def loopThroughCsv(csv):

    row_counter = 0
    split_number = 0

    for row in csv:

        column_headers = grabColumnHeaders(row)

        if (row_counter == 0) or (row_counter == split_threshold):
            split_number += 1
            write_csv = open(f'CSV_{split_number}.csv', 'w')
            writer = writeNewCsv(write_csv, column_headers, split_number)
            writer.writerow(row)

            row_counter = 0
        else:
            writer.writerow(row)

        row_counter += 1

with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    loopThroughCsv(csv_reader)