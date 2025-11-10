"""CP1404 Practical - Project Management Program
Estimated Time: 180 minutes
Actual time:
"""

import datetime

from project import Project

FILENAME = "projects.txt"
MENU = "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"
DATE_FORMAT = "%d/%m/%Y"

def main():
    """Main function for the Project Management Program"""
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    choice = input(f"\n{MENU}\n>>> ").lower()
    while choice != "q":
        if choice == "l":
            new_filename = input("Load projects from filename: ")
            projects = load_projects(new_filename)
        elif choice == "s":
            new_filename = input("Save projects to filename: ")
            save_projects(new_filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        else:
            print("Invalid menu choice")
        choice = input(f"\n{MENU}\n>>> ").lower()
    save_choice = input(f"Would you like to save to {FILENAME}? (y/n) ").lower()
    if save_choice == "y":
        save_projects(FILENAME, projects)
    else:
        print("Projects not saved.")

    print("Thank you for using custom-built project management software")


def load_projects(filename):
    """Load projects from filename"""
    projects = []
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split('\t')
                name = parts[0]
                start_date = datetime.datetime.strptime(parts[1], DATE_FORMAT).date()
                priority = int(parts[2])
                cost_estimate = float(parts[3])
                completion_percentage = int(parts[4])
                project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
        return projects
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except IndexError:
        print("Error: File is incorrectly formatted (missing fields).")
        return []


if __name__ == "__main__":
    main()
