# Student Record Management System

## Module 2 – Day 6 to Day 10

A beginner-friendly Python command-line project created for the Codomax Digital Solutions internship.

## Features

- Add student records
- View all students
- Search for a student
- Update student details
- Delete student records
- Store records in CSV
- Export records to JSON
- Read JSON records
- Functions and parameters
- List comprehensions
- Lambda functions
- Exception handling
- File handling

## Technologies

- Python
- CSV
- JSON
- Git and GitHub

## Run the Project

```bash
python student_manager.py
```

## Data Files

The program creates:

- `students.csv`
- `students.json`

The CSV file is used as the main storage file. JSON export is available from the menu.

## CRUD Operations

Create → Add Student

Read → View/Search Student

Update → Update Student

Delete → Delete Student

## Learning Topics

### Functions
The project uses functions with parameters and return values to organize the program.

### Lambda
Lambda expressions can be used for short operations, for example:

```python
square = lambda x: x * x
print(square(5))
```

### List Comprehension

```python
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(squares)
```

### Exception Handling

The project uses `try`, `except` and validation to handle invalid input and file errors safely.

### Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Activate on macOS/Linux:

```bash
source venv/bin/activate
```

Deactivate:

```bash
deactivate
```
