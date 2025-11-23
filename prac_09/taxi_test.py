"""
CP1404/CP5632 Practical
Client code to test the Taxi class functionality.
"""
from taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)
    print(f" Initial Taxi State ")
    print(f"Details: {my_taxi}")
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    print("-" * 30)
    print("ACTION: Driving 40 km (First trip)")
    my_taxi.drive(40)
    print(f"\nAfter 40 km Drive ")
    print(f"Details: {my_taxi}")
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    print("-" * 30)
    my_taxi.start_fare()
    print("ACTION: Meter restarted (start_fare())")
    print("ACTION: Driving 100 km (Second trip)")
    my_taxi.drive(100)
    print(f"\nAfter 100 km Drive (New Fare) ")
    print(f"Details: {my_taxi}")
    print(f"Current Fare: ${my_taxi.get_fare():.2f}")
    print("-" * 30)
    print(f"\nTotal Fuel Remaining: {my_taxi.fuel}")


if __name__ == '__main__':
    main()