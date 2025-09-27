def main():
    """This programme gets a password and prints asterisks based on the length of password"""
    user_input = get_password()
    if user_input == "Pythonista":
        print_asterisks(user_input)


def print_asterisks(user_input):
    """This function prints asterisks based on the length of password"""
    print(len(user_input) * "*")


def get_password():
    """This function gets a password from the user"""
    user_input = input("Enter a password: ")
    return user_input


main()
