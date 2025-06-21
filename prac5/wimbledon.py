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

def get_champions_counts(data):
    # Return a dictionary with champion names as keys and their win counts as values.
    counts = {}
    for row in data:
        champion = row[2]
        counts[champion] = counts.get(champion, 0) + 1
    return counts