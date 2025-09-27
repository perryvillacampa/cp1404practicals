"""
This programme shows a menu and says hello or goodbye based on the user input
"""

user_name = input("Enter name: ")
print("(H)ello\n(G)oodbye\n(Q)uit")
user_input = input(">>> ").upper()
while user_input != "Q":
    if user_input == "H":
        print("Hello " + user_name)
    elif user_input == "G":
        print("Goodbye " + user_name)
    else:
        print("Invalid choice")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    user_input = input(">>> ").upper()
print("Finished.")