# Creating a Student Information Dictionary
student = {
    "Name": "Ashrutha",
    "Age": 21,
    "Course": "B.Tech CSE",
    "City": "Hyderabad"
}

print("Original Dictionary:")
print(student)

# Accessing values
print("\nStudent Name:", student["Name"])
print("Student Age:", student["Age"])
print("Course:", student["Course"])
print("City:", student["City"])

# Adding a new key-value pair
student["College"] = "Malla Reddy University"
print("\nAfter adding College:")
print(student)

# Updating a value
student["City"] = "Karimnagar"
print("\nAfter updating City:")
print(student)

# Removing data
student.pop("Age")
print("\nAfter removing Age:")
print(student)

# Displaying keys
print("\nDictionary Keys:")
print(student.keys())

# Displaying values
print("\nDictionary Values:")
print(student.values())

# Displaying key-value pairs
print("\nDictionary Items:")
print(student.items())

# Checking whether a key exists
print("\nIs Name present?", "Name" in student)

# Dictionary length
print("Number of details:", len(student))