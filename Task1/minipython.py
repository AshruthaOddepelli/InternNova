name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
course = input("Enter Course: ")
marks = float(input("Enter Marks: "))

print("\n------ Student Information ------")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Course       :", course)
print("Marks        :", marks)

if marks >= 35:
    print("Result       : Pass")
else:
    print("Result       : Fail")