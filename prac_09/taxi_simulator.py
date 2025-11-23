"""
CP1404 Practical - Taxi Simulator.
Simulate a taxi service using the Taxi and SilverServiceTaxi classes.
Demonstrates polymorphism where the drive() and get_fare() methods
work differently based on the object's class.
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "(Q)uit, (C)hoose taxi, (D)rive"


def main():
    """Run the taxi simulator program."""
    total_bill = 0.0
    current_taxi = None
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_bill = drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the list of available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Allow the user to choose a taxi from the list."""
    print("Taxis available: ")
    display_taxis(taxis)
    while True:
        try:
            taxi_choice = int(input("Choose taxi: "))
            if 0 <= taxi_choice < len(taxis):
                chosen_taxi = taxis[taxi_choice]
                chosen_taxi.start_fare()
                return chosen_taxi
            else:
                print("Invalid taxi choice")
        except ValueError:
            print("Invalid taxi choice")


def drive_taxi(current_taxi, total_bill):
    """Handle the driving of the current taxi and update the bill."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return total_bill
    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance > 0:
                break
            print("Distance must be greater than 0")
        except ValueError:
            print("Invalid distance")
    current_taxi.drive(distance)
    trip_cost = current_taxi.get_fare()
    total_bill += trip_cost

    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
    current_taxi.start_fare()
    return total_bill


if __name__ == '__main__':
    main()