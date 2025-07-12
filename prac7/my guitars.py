from guitar import Guitar

def main():
    print("My guitars!")
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def load_guitars(filename):
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0].strip()
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars

FILENAME = "guitar.csv"
guitars = load_guitars(FILENAME)

def display_guitars(guitars):
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")