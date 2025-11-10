"""CP1404 Practical - Project Management Program
Estimated Time: 180 minutes
Actual time: 120 minutes
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


def filter_projects_by_date(projects):
    """Ask user for a date and display projects starting after that date, sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yy.")
        return
    filtered_projects = [p for p in projects if p.start_date >= filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Ask the user for new project details and add it to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    date_string = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    start_date = datetime.datetime.strptime(date_string, DATE_FORMAT).date()
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Choose a project, then modify its completion % and/or priority."""
    if not projects:
        print("No projects to update.")
        return
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice_index = int(input("Project choice: "))
        if 0 <= choice_index < len(projects):
            project_to_update = projects[choice_index]
            print(project_to_update)
            new_percentage_input = input("New Percentage: ")
            if new_percentage_input != "":
                project_to_update.completion_percentage = int(new_percentage_input)
            new_priority_input = input("New Priority: ")
            if new_priority_input != "":
                project_to_update.priority = int(new_priority_input)
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input for choice, percentage, or priority.")\


if __name__ == "__main__":
    main()
