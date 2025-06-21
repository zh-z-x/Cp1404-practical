"""
Wimbledon
Estimate: 40 minutes
Actual:  minutes
"""

import csv

def read_wimbledon_data(filename):
    #Read the CSV file and return a list of rows (each row is a list of fields).
    data = []
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            data.append(row)
    return data
