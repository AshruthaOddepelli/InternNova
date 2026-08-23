#What is Scope?

#Scope means where a variable can be accessed or used in a Python program.

#There are two important types for your task:

#1. Local Variable

#A variable created inside a function is called a local variable.

x = 20          # Global variable

def demo():
    x = 10      # Local variable
    print("Local:", x)

demo()

print("Global:", x)
