"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs in the numerator and denominator user input when there are texts or letters in the input. FOr example, "12a" or "3.14"
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the program attempts to perform the division operation and the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes you can add an error checking loop to ensure that the user enters valid integers
"""

def main():
    try:
        numerator = get_valid_integer("Enter the numerator", 0)
        denominator = get_valid_integer("Enter the denominator", 0)
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_valid_integer(prompt, low):
    number = int(input(prompt))
    while number <= low:
        print("Please enter a valid integer!")
        number = int(input(prompt))
    return number


main()