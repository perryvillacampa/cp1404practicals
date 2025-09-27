def main():
    """This program is a score checker and prints stars based on your score"""
    print("(G)et Score\n(P)rint Result\n(S)how Stars\n(Q)uit")
    menu_choice = input(">> ").upper()
    score = ""
    while menu_choice != "Q":
        if menu_choice == "G":
            score = get_valid_score(0, 100, "Enter subject score: ")
        elif menu_choice == "P":
            result = determine_result(score)
            print(f"Your score is {result}.")
        elif menu_choice == "S":
            print_stars(score)
        print("(G)et Score\n(P)rint Result\n(S)how Stars\n(Q)uit")
        menu_choice = input(">> ").upper()
    print("Farewell")


def print_stars(score):
    """Prints * based on the subject score."""
    print(int(score) * "*")


def determine_result(subject_score):
    """Determines the subject score"""
    if subject_score >= 90:
        return "Excellent"
    elif subject_score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_score(low, high, prompt):
    """Gets a valid score from the user between low and high."""
    score = int(input(prompt))
    while score < low or score > high:
        print("Please enter a valid score.")
        score = int(input(prompt))
    return score


main()

