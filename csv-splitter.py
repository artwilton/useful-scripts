import csv

csv_file_path = "/Users/arthur/Desktop/csv_test.csv"
split_threshold = input('Enter how many rows per CSV file you would like: ')

def loopThroughCsv(csv):
    column_headers = []
    row_counter = 0
    split_number = 1

    for row in csv:

        if row_counter == 0:
            column_headers = row
            print(f"column headers = {column_headers}")
        else:
            if row_counter > split_threshold:
                split_number += 1
                print(f"write new row to csv{split_number}")
                row_counter = 1
            else:
                print(f"write new row to csv{split_number}")

        row_counter += 1
        print(f"row counter: {row_counter}")

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    loopThroughCsv(csv_reader)