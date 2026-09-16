# Task 2: Constructors

class Student:

    # Constructor
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    # Method to display student information
    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("----------------------")


# Creating objects with different values
student1 = Student("Ashrutha", 101, "B.Tech CSE", 85)
student2 = Student("Anjali", 102, "B.Tech CSE", 90)

# Accessing initialized attributes
print("First Student:")
student1.display_info()

print("Second Student:")
student2.display_info()

