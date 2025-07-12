import datetime
import os
from project import Project

def main():
    default_filename = "projects.txt"
    projects = load_projects(default_filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {default_filename}")

    running = True
    while running:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save: ")
            if filename:
                save_projects(projects, filename)
                print(f"Saved to {filename}")
            else:
                print("Invalid filename.")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {default_filename}? ").lower()
            if save_choice.startswith('y'):
                save_projects(projects, default_filename)
                print(f"Saved to {default_filename}")
            print("Thank you for using custom-built project management software.")
            running = False
        else:
            print("Invalid choice.")


def load_projects(filename):
    projects = []
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        return projects

    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        if lines:
            lines = lines[1:]
            for line in lines:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name, date_str, priority, cost, completion = parts
                    if is_valid_date(date_str):
                        date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                        if (is_valid_number(priority) and
                                is_valid_number(cost) and
                                is_valid_number(completion)):
                            project = Project(name, date, priority, cost, completion)
                            projects.append(project)
    return projects

def save_projects(projects, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                      f"{project.priority}\t{project.cost_estimate}\t{project.completion}\n")

def is_valid_date(date_str):
    parts = date_str.split('/')
    if len(parts) != 3:
        return False
    day, month, year = parts
    return (day.isdigit() and month.isdigit() and year.isdigit() and
            1 <= int(day) <= 31 and 1 <= int(month) <= 12 and len(year) == 4)

def is_valid_number(value):
    if not value:
        return False
    parts = value.split('.')
    if len(parts) > 2:
        return False
    return all(part.isdigit() for part in parts)


def display_projects(projects):
    incomplete = sorted([p for p in projects if not p.is_completed()], key=lambda x: x.priority)
    completed = sorted([p for p in projects if p.is_completed()], key=lambda x: x.priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):

    date_input = input("Show projects that start after date (dd/mm/yy): ")
    if not is_valid_date(date_input):
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    date = datetime.datetime.strptime(date_input, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.start_date > date], key=lambda x: x.start_date)
    for project in filtered:
        print(f"  {project}")


def add_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    date_str = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    completion = input("Percent complete: ")

    if not name or not is_valid_date(date_str):
        print("Invalid input. Project not added.")
        return
    if not priority:
        priority = "1"
    if not cost:
        cost = "0.0"
    if not completion:
        completion = "0"
    if not (is_valid_number(priority) and is_valid_number(cost) and is_valid_number(completion)):
        print("Invalid input. Project not added.")
        return

    date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
    cost = float(cost.replace('$', '')) if '$' in cost else float(cost)
    completion = int(completion)
    priority = int(priority)
    projects.append(Project(name, date, priority, cost, completion))

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = input("Project choice: ")

    if not choice.isdigit() or not (0 <= int(choice) < len(projects)):
        print("Invalid project choice.")
        return

    project = projects[int(choice)]
    print(project)
    completion = input("New Percentage: ")
    priority = input("New Priority: ")

    if completion and not is_valid_number(completion):
        print("Invalid completion percentage.")
        return
    if priority and not is_valid_number(priority):
        print("Invalid priority.")
        return

    project.update(completion=completion or None, priority=priority or None)

if __name__ == "__main__":
    main()