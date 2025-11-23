"""
CP1404/CP5632 Practical
UnreliableCar class, a specialised version of a Car that randomly fails to drive.
"""
import random
from car import Car

class UnreliableCar(Car):
    """Represent an UnreliableCar object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car. reliability: float, percentage chance (0-100) that the car will drive."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation of the unreliable car, including reliability"""
        return f"{super().__str__()} ({self.reliability:.1f}%)"

    def drive(self, distance):
        """Drive the car based on distance only if a random number form 0-100 is less than the car's reliability."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
            print(f"{self.name} failed to drive (Rolled {random_number:.2f}), Reliability {self.reliability:.1f}%")
        return distance_driven