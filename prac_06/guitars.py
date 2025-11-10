"""
CP1404 Practical - Client program for the Guitar class.

Estimate: 40 minutes
Actual: 50 minutes
"""
from guitar import Guitar


def main():
    """Read guitar information until a blank name is entered, then display the list."""
    guitars = []
    print("My guitars!")
    # name = input("Name: ")
    # while name != "":
    #     try:
    #         year = int(input("Year: "))
    #         cost = float(input("Cost: $"))
    #         guitar = Guitar(name, year, cost)
    #         guitars.append(guitar)
    #         print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
    #     except ValueError:
    #         print("Invalid input for year or cost. Please try again.")
    #     name = input("\nName: ")
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

    if not guitars:
        print("No guitars added. Goodbye!")
        return
    guitars.sort(key=lambda g: g.year)

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
