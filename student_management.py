"""Mini Project: manage students in a CSV file."""

import csv
from pathlib import Path

# Keep the CSV file beside this Python script.
CSV_FILE = Path(__file__).with_name("students.csv")
HEADERS = ["roll_number", "name", "marks"]


def read_students():
    """Read all students from the CSV file into a list of dictionaries."""
    if not CSV_FILE.exists():
        return []

    try:
        with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))
    except OSError as error:
        print(f"Could not read the student file: {error}")
        return []


def save_students(students):
    """Save the full student list to CSV, including its header row."""
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
            writer.writerows(students)
        return True
    except OSError as error:
        print(f"Could not save the student file: {error}")
        return False


def show_students(students):
    """Display one or more students."""
    if not students:
        print("No students found.")
        return

    print("\nRoll number | Name | Marks")
    print("-" * 32)
    for student in students:
        print(f"{student['roll_number']} | {student['name']} | {student['marks']}")


def add_student():
    students = read_students()
    roll_number = input("Enter roll number: ").strip()

    if not roll_number:
        print("Roll number cannot be empty.")
        return
    if any(student["roll_number"] == roll_number for student in students):
        print("That roll number is already in use.")
        return

    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0 to 100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter marks as a number.")
        return

    # Add the new row and save the complete list to keep it permanently.
    students.append({"roll_number": roll_number, "name": name, "marks": str(marks)})
    if save_students(students):
        print("Student added to students.csv.")


def search_student():
    roll_number = input("Enter roll number to search: ").strip()
    matches = [
        student for student in read_students()
        if student["roll_number"] == roll_number
    ]
    show_students(matches)


def delete_student():
    students = read_students()
    roll_number = input("Enter roll number to delete: ").strip()
    remaining_students = [
        student for student in students
        if student["roll_number"] != roll_number
    ]

    if len(remaining_students) == len(students):
        print("Student not found.")
    elif save_students(remaining_students):
        print("Student deleted from students.csv.")


def main():
    while True:
        print("\nSTUDENT MANAGEMENT SYSTEM")
        print("1. Add student")
        print("2. Search student")
        print("3. Delete student")
        print("4. Show all students")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            show_students(read_students())
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from the menu.")


if __name__ == "__main__":
    main()
