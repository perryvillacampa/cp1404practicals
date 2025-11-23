"""
CP1404/CP5632 Practical
SilverServiceTaxi class, a specialised version of a Taxi with a fanciness factor
and an added flag fall charge.
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a SilverServiceTaxi object."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with the flag fall charge."""
        return f"{super().__str__()} plus flag fall of ${self.flag_fall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip, including the flag fall."""
        fare = super().get_fare()
        return fare + self.flag_fall