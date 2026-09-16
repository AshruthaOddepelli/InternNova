# Student Management System

## Project Description

The Student Management System is a Python-based console application developed as the Week 6 Final Project.

It allows users to manage student information such as student ID, name, age, course, marks, and grades.

The project demonstrates Python programming concepts learned throughout the internship, including functions, data structures, file handling, exception handling, and Object-Oriented Programming.

## Features

- Add student
- View all students
- Search student
- Update student marks
- Delete student
- Calculate student grade
- Save student data
- Load student data
- Exception handling
- File handling
- Menu-driven interface

## Technologies Used

- Python 3
- JSON
- Object-Oriented Programming

## Python Concepts Used

- Variables and Data Types
- Input and Output
- Operators
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- File Handling
- JSON
- Exception Handling
- Classes and Objects
- Constructors
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

## OOP Concepts

### Classes and Objects
The `Student` class represents a student, and objects are created for individual students.

### Constructor
The `__init__()` method initializes student details.

### Inheritance
The `Student` class inherits from the `Person` class.

### Polymorphism
The `display_role()` method is implemented in the `Student` class.

### Encapsulation
Student marks are stored using the private attribute `__marks`.

Controlled access is provided using:

- `get_marks()`
- `update_marks()`

### Abstraction
The `Person` class is an abstract class using `ABC` and `@abstractmethod`.

## Installation / Setup

1. Install Python 3.

2. Clone or download the project.

3. Open the project folder in VS Code.

4. Run the following command:

```bash
python main.py