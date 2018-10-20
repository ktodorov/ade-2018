import csv
import numpy as np

def open_file(csvfile):
    with open(csvfile, 'rt') as file:
        suppliers = []
        file = csv.reader(file, delimiter='\n', quotechar='|')
        for row in file:
            row = row[0].split(",")
            suppliers.append(row)
        return suppliers

suppliers_list = open_file("test_data.csv")

