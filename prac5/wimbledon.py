"""
Wimbledon
Estimate: 40 minutes
Actual: 38 minutes
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

def get_countries(data):
    # Return a sorted list of unique champion countries.
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return sorted(countries)

def main():
    filename = "wimbledon.csv"
    data = read_wimbledon_data(filename)

    champions_counts = get_champions_counts(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for champion, count in sorted(champions_counts.items()):
        print(f"{champion} {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))

if __name__ == "__main__":
    main()