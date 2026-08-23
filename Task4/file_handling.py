# Create and write data into a file
file = open("student.txt", "w")

file.write("Name: Ashrutha\n")
file.write("Course: B.Tech CSE\n")
file.write("Subject: Python\n")

file.close()

# Read and display file content
file = open("student.txt", "r")

print("Original File Content:")
print(file.read())

file.close()

# Append new data
file = open("student.txt", "a")

file.write("Topic: File Handling\n")
file.write("Week: 4\n")

file.close()

# Display updated content
file = open("student.txt", "r")

print("\nUpdated File Content:")
print(file.read())

file.close()