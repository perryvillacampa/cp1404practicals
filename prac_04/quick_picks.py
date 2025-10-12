"""
CP1404 Practical
Quick Pick Lottery Ticket Generator

Generates a specified number of unique, sorted quick pick lines.
"""
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6
MAX_QUICK_PICKS = 20


def main():
    """Get the number of quick picks and generate the random numbers."""
    print(f"Generate lottery quick picks with {NUMBERS_PER_PICK} unique numbers "
          f"between {MIN_NUMBER} and {MAX_NUMBER}.")
    number_of_quick_picks = get_valid_number_of_picks()
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def get_valid_number_of_picks():
    """Prompts the user for the number of quick picks and ensures input is valid."""
    is_valid_input = False
    while not is_valid_input:
        try:
            picks = int(input("How many quick picks? "))
            if picks <= 0:
                print("The number of picks must be greater than zero.")
            elif picks > MAX_QUICK_PICKS:
                print(f"Please enter a number less than or equal to {MAX_QUICK_PICKS}.")
            else:
                is_valid_input = True
                return picks
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def generate_quick_pick():
    """
    Generates a single quick pick line containing NUMBERS_PER_PICK unique,
    random numbers between MIN_NUMBER and MAX_NUMBER, and returns them sorted.
    """
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()