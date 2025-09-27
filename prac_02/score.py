import random

def main():
    """This program gets a subject score and determines its result"""
    subject_score = get_valid_subject_score()
    result = determine_result(subject_score)
    random_score = random.randint(0, 101)
    determine_result(random_score)
    print(f"The subject score is: {subject_score} and its {result}.")
    print(f"The random score is: {random_score} and its {determine_result(random_score)}.")


def determine_result(subject_score):
    """Determines the subject score"""
    if subject_score >= 90:
        return "Excellent"
    elif subject_score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_valid_subject_score():
    """Gets a valid subject score"""
    subject_score = float(input("Enter score: "))
    while subject_score <= 0 or subject_score >= 100:
        print("Invalid score")
        subject_score = float(input("Enter score: "))
    return subject_score


main()

