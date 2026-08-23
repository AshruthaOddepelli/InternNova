# Handling invalid user input
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Error: Please enter a valid number.")


# Handling division by zero
try:
    num1 = int(input("\nEnter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")


# Handling file not found
try:
    file = open("unknown.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: The requested file was not found.")