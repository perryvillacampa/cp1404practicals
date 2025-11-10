"""
CP1404 Practical - My Guitars program.
Reads and stores Guitar objects from a CSV file, allows new input, sorts, and saves.
"""
from guitar import Guitar

FILENAME = "guitars.csv"

def main():
    """Program to read, display, sort, add and save a list of Guitar objects."""
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)
    get_new_guitars(guitars)
    save_guitars(guitars)


def load_guitars():
    """Reads guitars from the CSV file and returns a list of Guitar objects."""
    guitars = []
    try:
        with open(FILENAME, 'r') as in_file:
            for line in in_file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    continue
                try:
                    name = parts[0]
                    year = int(parts[1])
                    cost = float(parts[2])
                    guitar = Guitar(name, year, cost)
                    guitars.append(guitar)
                except ValueError:
                    print(f"Skipping badly formatted line: {line.strip()}")
        print(f"Loaded {len(guitars)} guitars from {FILENAME}.")
        return guitars
    except FileNotFoundError:
        print(f"{FILENAME} not found. Starting with an empty list.")
        return []


def display_guitars(guitars):
    """ Display the list of Guitar objects with formatting."""
    print("Displaying Guitars")
    if not guitars:
        print("No guitars found.")
        return
    guitars.sort()
    for i, guitar in enumerate(guitars, 1):
        vintage_status = "(VINTAGE)" if guitar.is_vintage() else ""
        print(f"Guitar{i}: {guitar.name:<25} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_status}")


def get_new_guitars(guitars):
    """Prompts the user for new guitars and adds them to the list."""
    print("\n... Add New Guitars ...")
    name = input("Enter new guitar name (or blank to stop): ")
    while name != "":
        try:
            year = int(input("Year: "))
            while year < 1000 or year > Guitar.CURRENT_YEAR:
                print(f"Please enter a valid year (e.g., between 1000 and {Guitar.CURRENT_YEAR})")
                year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"{new_guitar.name} ({new_guitar.year}) added.")
        except ValueError:
            print("Invalid input for year or cost. Please use numbers.")
        name = input("Enter new guitar name (or blank to stop): ")


if __name__ == "__main__":
    main()