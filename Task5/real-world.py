# Task 1: Classes and Objects

class Student:
    # Method to display student information
    def display_info(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("----------------------")


# Creating first object
student1 = Student()
student1.name = "Ashrutha"
student1.roll_no = 101
student1.course = "B.Tech CSE"
student1.marks = 85

# Creating second object
student2 = Student()
student2.name = "Anjali"
student2.roll_no = 102
student2.course = "B.Tech CSE"
student2.marks = 90

# Displaying information
student1.display_info()
student2.display_info()