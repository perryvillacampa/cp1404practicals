"""
Emails
Estimate: 30 minutes
Actual:   45 minutes
Program to store user emails and names in a dictionary.
Uses a separate function to extract a suggested name from the email address.

CP1404 Practical
"""

def main():
    """Main function to collect emails and names and display the dictionary."""
    email_to_name = {}
    print("--- Email and Name Collector ---")
    email = input("Email: ")
    while email != "":
        email = email.lower()
        suggested_name = extract_name_from_email(email)
        prompt = f"Is your name {suggested_name}? (Y/n) "
        confirmation = input(prompt).lower()
        if confirmation == "" or confirmation == "y":
            name = suggested_name
        else:
            name = input("Name: ")
            name = name.title()
        email_to_name[email] = name
        email = input("Email: ")
    print("\n--- Stored Users ---")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

    print("\nProgram finished.")


def extract_name_from_email(email):
    """ Extracts a suggested name from the email address."""
    parts = email.split('@')
    name_part = parts[0]
    name_part = name_part.replace('.', ' ').replace('_', ' ')
    name = name_part.title()
    return name


main()