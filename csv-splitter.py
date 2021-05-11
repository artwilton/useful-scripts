"""
This script takes in two inputs, a path to a csv file and the amount of rows a user wants to split that csv file into.
The column headers will be copied over to the first row of each csv file.
"""

import csv

def write_new_csv(csv_file_write, column_headers, split_number):

    writer = csv.DictWriter(csv_file_write, fieldnames=column_headers)
    writer.writeheader()

    return writer

def loop_through_csv(csv, split_threshold, column_headers):

    row_counter = 0
    split_number = 0
    write_csv = None

    for row in csv:

        if (row_counter == 0) or (row_counter == split_threshold):

            # close file if it already exists before writing to a new csv file
            if write_csv:
                write_csv.close()

            split_number += 1
            write_csv = open(f'CSV_{split_number}.csv', 'w')
            writer = write_new_csv(write_csv, column_headers, split_number)
            writer.writerow(row)
            row_counter = 0
        else:
            writer.writerow(row)

        row_counter += 1

def main():

    # grab inputs from user
    csv_file_path = input('Enter csv file path: ')
    split_threshold = int(input('Enter how many rows per CSV file you would like: '))

    with open(csv_file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        column_headers = csv_reader.fieldnames
        loop_through_csv(csv_reader, split_threshold, column_headers)

if __name__ == "__main__":
    main()