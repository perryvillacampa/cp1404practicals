
def main():
    user_input = get_password()
    if user_input == "Pythonista":
        print_asterisks(user_input)


def print_asterisks(user_input):
    print(len(user_input) * "*")


def get_password():
    user_input = input("Enter a password: ")
    return user_input


main()
