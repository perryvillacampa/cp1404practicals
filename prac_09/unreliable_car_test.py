"""
CP1404/CP5632 Practical
Client code to test the UnreliableCar class functionality.
Since functionality involves randomness, we test multiple iterations.
"""
from unreliable_car import UnreliableCar

ATTEMPTS = 100
DISTANCE_TO_DRIVE = 10

def main():
    low_reliability_car = UnreliableCar("LowReliable", 100, 30)
    high_reliability_car = UnreliableCar("HighReliable", 100, 90)
    broken_car = UnreliableCar("BrokenCar", 100, 0)
    perfect_car = UnreliableCar("PerfectCar", 100, 100)
    cars = [low_reliability_car, high_reliability_car, broken_car, perfect_car]
    print(f"Testing UnreliableCar Over {ATTEMPTS} Attempts")
    print(f"Attempting to drive {DISTANCE_TO_DRIVE} km each time.")
    for attempt in range(1, ATTEMPTS + 1):
        if attempt % 20 == 0:
            print(f"\nAttempt {attempt}")
        for car in cars:
            distance_driven = car.drive(DISTANCE_TO_DRIVE)
            print(f"[{car.name:15}]: Drove {distance_driven:2} km. Odometer: {car._odometer:3}km")
    print("\nSummary of Test Results")
    for car in cars:
        total_distance = car._odometer
        max_possible_distance = ATTEMPTS * DISTANCE_TO_DRIVE
        percentage_driven = (total_distance / max_possible_distance) * 100 if max_possible_distance > 0 else 0
        print(f"\n{car.name} (Target Reliability: {car.reliability:.1f}%)")
        print(f"  Total Distance Driven: {total_distance} km (out of {max_possible_distance} km possible)")
        print(f"  Actual Success Rate: {percentage_driven:.1f}%")


if __name__ == "__main__":
    main()