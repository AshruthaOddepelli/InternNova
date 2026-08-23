# Creating a tuple
numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)

# Accessing elements using indexing
print("First element:", numbers[0])
print("Third element:", numbers[2])

# Tuple slicing
print("First three elements:", numbers[:3])
print("Last two elements:", numbers[-2:])

# Finding length
print("Length of tuple:", len(numbers))

# Basic tuple operations
tuple2 = (60, 70, 80)

print("Second Tuple:", tuple2)

# Concatenation
combined = numbers + tuple2
print("Combined Tuple:", combined)

# Repetition
print("Repeated Tuple:", (1, 2) * 3)

# Membership
print("Is 30 present?", 30 in numbers)