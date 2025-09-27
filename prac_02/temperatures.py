def main():
    """This program converts Celsius to Fahrenheit. Vice versa"""
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_user_input("Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_user_input("Fahrenheit: ")
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """This function converts Celsius to Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius(fahrenheit):
    """This function converts Fahrenheit to Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def display_menu():
    """This function displays the menu."""
    menu = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(menu)
    return menu


def get_user_input(prompt):
    """This function gets user input."""
    user_input = float(input(prompt))
    return user_input


main()

