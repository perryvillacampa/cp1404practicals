"""
CP1404/CP5632 Practical
Band class for demonstrating the "has a" (association/aggregation) relationship.
A Band 'has a' list of Musician objects.
"""


class Band:
    """Band class that stores a collection of Musician objects."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band and its musicians."""
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a Musician object to the band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """
        Return a string showing each musician in the band playing their primary instrument.
        """
        play_messages = [musician.play() for musician in self.musicians]
        return "\n".join(play_messages)


if __name__ == '__main__':
    from musician import Musician
    band = Band("The Test Band")
    john = Musician("John")
    paul = Musician("Paul")
    band.add(john)
    band.add(paul)
    print(band)
    print(band.play())