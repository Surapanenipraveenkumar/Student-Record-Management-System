import csv
import json
from pathlib import Path

CSV_FILE = Path("students.csv")
JSON_FILE = Path("students.json")


def add_student(student_id, name, age, course, email):
    students = load_students()
    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return
    students.append({
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "email": email
    })
    save_students(students)
    print("Student added successfully.")


def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    for student in students:
        print(
            f'ID: {student["id"]} | Name: {student["name"]} | '
            f'Age: {student["age"]} | Course: {student["course"]} | '
            f'Email: {student["email"]}'
        )


def search_student(student_id):
    students = load_students()
    student = next((s for s in students if s["id"] == student_id), None)
    if student:
        print(student)
    else:
        print("Student not found.")


def update_student(student_id):
    students = load_students()
    student = next((s for s in students if s["id"] == student_id), None)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    student["name"] = input(f'Name [{student["name"]}]: ') or student["name"]
    student["age"] = input(f'Age [{student["age"]}]: ') or student["age"]
    student["course"] = input(f'Course [{student["course"]}]: ') or student["course"]
    student["email"] = input(f'Email [{student["email"]}]: ') or student["email"]

    save_students(students)
    print("Student updated successfully.")


def delete_student(student_id):
    students = load_students()
    updated = [s for s in students if s["id"] != student_id]

    if len(updated) == len(students):
        print("Student not found.")
        return

    save_students(updated)
    print("Student deleted successfully.")


def load_students():
    if CSV_FILE.exists():
        try:
            with CSV_FILE.open("r", newline="", encoding="utf-8") as file:
                return list(csv.DictReader(file))
        except (csv.Error, OSError):
            print("CSV file could not be read. Starting with empty records.")
            return []
    return []


def save_students(students):
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "name", "age", "course", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)
    except OSError as error:
        print(f"File error: {error}")


def export_json():
    students = load_students()
    try:
        with JSON_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
        print("Records exported to students.json.")
    except OSError as error:
        print(f"JSON file error: {error}")


def show_json():
    if not JSON_FILE.exists():
        print("students.json does not exist.")
        return
    try:
        with JSON_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        print(json.dumps(data, indent=4))
    except (json.JSONDecodeError, OSError) as error:
        print(f"JSON error: {error}")


def menu():
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Export to JSON")
        print("7. View JSON")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                student_id = input("Student ID: ").strip()
                name = input("Name: ").strip()
                age = input("Age: ").strip()
                if not age.isdigit():
                    raise ValueError("Age must be a number.")
                course = input("Course: ").strip()
                email = input("Email: ").strip()
                if not all([student_id, name, course, email]):
                    raise ValueError("All fields are required.")
                add_student(student_id, name, age, course, email)

            elif choice == "2":
                view_students()

            elif choice == "3":
                student_id = input("Enter Student ID: ").strip()
                search_student(student_id)

            elif choice == "4":
                student_id = input("Enter Student ID: ").strip()
                update_student(student_id)

            elif choice == "5":
                student_id = input("Enter Student ID: ").strip()
                delete_student(student_id)

            elif choice == "6":
                export_json()

            elif choice == "7":
                show_json()

            elif choice == "8":
                print("Program closed.")
                break

            else:
                print("Invalid choice.")

        except ValueError as error:
            print(f"Input error: {error}")
        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    menu()
