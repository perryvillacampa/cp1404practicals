"""
CP1404/CP5632 Practical - Guitar class testing.

Estimate: 20 minutes
Actual: 25 minutes
"""
from guitar import Guitar, CURRENT_YEAR


def run_tests():
    """Test the Guitar methods (get_age() and is_vintage())."""
    print("Guitar Class Tests:")

    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)

    another_name = "Another Guitar"
    another_year = 2013
    another_guitar = Guitar(another_name, another_year)

    print(f"\nCurrent Year: {CURRENT_YEAR}")

    expected_age_vintage = CURRENT_YEAR - year
    expected_age_modern = CURRENT_YEAR - another_year

    print(f"{name} get_age() - Expected {expected_age_vintage}. Got {guitar.get_age()}")
    print(f"{another_name} get_age() - Expected {expected_age_modern}. Got {another_guitar.get_age()}")

    print(f"{name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{another_name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


    border_year = CURRENT_YEAR - 50
    vintage_border_guitar = Guitar("Borderline Vintage", border_year)
    print(f"\n{vintage_border_guitar.name} ({border_year}) is_vintage() - Expected True. Got {vintage_border_guitar.is_vintage()}")


if __name__ == '__main__':
    run_tests()
