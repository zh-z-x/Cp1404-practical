from guitar import Guitar

def main():
    print("My guitars!")

    guitars = load_guitars(FILENAME)

    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    new_guitar = add_guitar()
    if new_guitar:
        guitars.append(new_guitar)

    save_guitars("guitar.csv", guitars)
    print(f"\nSaved {len(guitars)} guitars to guitar.csv.")

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

guitars.sort()
print("\nGuitars sorted by year:")
display_guitars(guitars)

def add_guitar():
    print("\nAdd a new guitar")
    name = input("Name: ").strip()
    year_input = input("Year: ").strip()
    cost_input = input("Cost: ").strip()
    if year_input.isdigit() and cost_input.replace('.', '', 1).isdigit():
        year = int(year_input)
        cost = float(cost_input)
        return Guitar(name, year, cost)
    else:
        print("Invalid input. Skipping.")
        return None

def save_guitars(filename, guitars):
    out_file = open(filename, 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()

if __name__ == "__main__":
    main()