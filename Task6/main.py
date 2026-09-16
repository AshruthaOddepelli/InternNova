from abc import ABC, abstractmethod
import json


# Abstraction
class Person(ABC):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_role(self):
        pass


# Inheritance
class Student(Person):

    def __init__(self, student_id, name, age, course, marks):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
        self.__marks = marks       # Encapsulation

    # Controlled access to private data
    def get_marks(self):
        return self.__marks

    def update_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Marks must be between 0 and 100.")

    # Polymorphism
    def display_role(self):
        print("Role: Student")

    def calculate_grade(self):
        marks = self.__marks

        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    def display_student(self):
        print("\n----- Student Details -----")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.get_marks())
        print("Grade:", self.calculate_grade())
        self.display_role()


# File Handling
students = []


def add_student():
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student = Student(student_id, name, age, course, marks)
        students.append(student)

        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Please enter correct values.")


def view_students():
    if not students:
        print("\nNo students available.")
        return

    for student in students:
        student.display_student()


def search_student():
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student.student_id == student_id:
            student.display_student()
            return

    print("Student not found.")


def update_student_marks():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student.student_id == student_id:
            try:
                marks = float(input("Enter new marks: "))
                student.update_marks(marks)
            except ValueError:
                print("Please enter a valid number.")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def save_students():
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.get_marks()
        })

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student data saved successfully.")


def load_students():
    global students

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        students = []

        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )
            students.append(student)

        print("Student data loaded successfully.")

    except FileNotFoundError:
        print("No saved student data found.")

    except json.JSONDecodeError:
        print("Invalid data file.")


def main():
    load_students()

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Save Students")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student_marks()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            save_students()

        elif choice == "7":
            save_students()
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()