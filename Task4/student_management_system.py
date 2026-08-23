import json
from datetime import datetime

FILE_NAME = "students.json"


# Load students from file
def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error: Student file contains invalid data.")
        return []


# Save students to file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a student
def add_student(students):
    print("\n--- Add Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        city = input("Enter city: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course,
            "city": city,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        students.append(student)
        save_students(students)

        print("Student added successfully.")

    except ValueError:
        print("Error: ID and age must be numbers.")


# Display students
def view_students(students):
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("City:", student["city"])
        print("Created At:", student["created_at"])


# Search student
def search_student(students):
    print("\n--- Search Student ---")

    name = input("Enter student name: ")

    found = False

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("City:", student["city"])

            found = True

    if not found:
        print("Student not found.")


# Delete student
def delete_student(students):
    print("\n--- Delete Student ---")

    try:
        student_id = int(input("Enter student ID: "))

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                save_students(students)

                print("Student deleted successfully.")
                return

        print("Student ID not found.")

    except ValueError:
        print("Error: Student ID must be a number.")


# Main program
def main():
    students = load_students()

    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            delete_student(students)

        elif choice == "5":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


# Start program
main()