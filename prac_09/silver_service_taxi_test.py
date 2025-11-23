"""
CP1404/CP5632 Practical
Client code to test the SilverServiceTaxi class functionality.
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    print("--- Test 1: Basic 10km trip (Fanciness 2) ---")
    premium_taxi = SilverServiceTaxi("Hummer", 200, 2)
    print(f"Details: {premium_taxi}")
    premium_taxi.drive(10)
    fare = premium_taxi.get_fare()
    print(f"Distance: 10km | Calculated Fare: ${fare:.2f}")
    assert fare == 29.1, "Test 1 failed: Fare calculation is incorrect."
    print("Test 1 Passed: Fare is correct ($29.10).")
    print("\n" + "=" * 50)
    print("--- Test 2: 18km trip (Fanciness 2) ---")
    luxury_taxi = SilverServiceTaxi("Limousine", 100, 2)
    print(f"Details before trip: {luxury_taxi}")
    luxury_taxi.drive(18)
    fare = luxury_taxi.get_fare()
    print(f"Distance: 18km | Calculated Fare: ${fare:.2f}")
    print(f"Expected unrounded distance cost: $44.28")
    print(f"Expected rounded distance cost: $44.30")
    print(f"Expected final fare: $44.30 + $4.50 = $48.80")
    assert fare == 48.8, "Test 2 failed: Fare calculation is incorrect."
    print("Test 2 Passed: Fare is correctly rounded and includes flagfall ($48.80).")
    print("\n" + "=" * 50)
    print("--- Test 3: String Representation (Fanciness 4) ---")
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)

if __name__ == "__main__":
    main()