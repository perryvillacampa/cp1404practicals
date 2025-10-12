"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_lists = get_subject_data(FILENAME)
    display_subject_details(subject_lists)


def get_subject_data(filename):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_data_list = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subject_data_list.append(parts)
    return subject_data_list


def display_subject_details(subject_list):
    """Display subject details."""
    print("\n--- Subject Details ---")
    for subject in subject_list:
        subject_code = subject[0]
        lecturer_name = subject[1]
        student_count = subject[2]
        print(f"{subject_code} is taught by {lecturer_name:<12} and has {student_count:3} students.")


main()
