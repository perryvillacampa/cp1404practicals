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


def save_projects(filename, projects):
    """Saves projects to a file."""
    try:
        with open(filename, 'w', encoding="utf-8") as out_file:
            out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                out_file.write(f"{project.name}\t{project.start_date.strftime(DATE_FORMAT)}\t"
                               f"{project.priority}\t{project.cost_estimate}\t"
                               f"{project.completion_percentage}\n")
        print(f"Saved {len(projects)} projects to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")


def display_projects(projects):
    """Display incomplete and completed projects, both sorted by priority."""
    print("\nIncomplete projects: ")
    incomplete_projects = [p for p in projects if not p.is_complete()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print(f"  {project}")
    print("Completed projects: ")
    completed_projects = [p for p in projects if p.is_complete()]
    completed_projects.sort()
    for project in completed_projects:
        print(f"  {project}")


if __name__ == "__main__":
    main()
