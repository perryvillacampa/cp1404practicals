"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car",180)
    my_car.drive(30)
    print(my_car)
    print("-" *20)
    limo = Car("Limo", 100)
    print(f"{limo.name} has fuel: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"The {limo.name} drove {distance_driven}km.")
    print(limo)


main()
