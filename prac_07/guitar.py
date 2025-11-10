CURRENT_YEAR = 2024

class Guitar:
    """Represent a Guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """
        Initialise a Guitar instance.
        name: string, name of the guitar
        year: integer, year the guitar was made
        cost: float, cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """
        Less than for Guitar objects, based on year (oldest first).
        This enables the list.sort() function.
        """
        return self.year < other.year

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
