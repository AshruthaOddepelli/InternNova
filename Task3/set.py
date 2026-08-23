# Creating a set
numbers = {10, 20, 30, 20, 40, 30}

print("Original Set:", numbers)

# Duplicate values are automatically removed
print("Duplicates removed:", numbers)

# Adding an element
numbers.add(50)
print("After adding 50:", numbers)

# Removing an element
numbers.remove(20)
print("After removing 20:", numbers)

# Creating another set
set2 = {30, 40, 50, 60, 70}

# Union
print("Union:", numbers.union(set2))

# Intersection
print("Intersection:", numbers.intersection(set2))

# Difference
print("Difference:", numbers.difference(set2))