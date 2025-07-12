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