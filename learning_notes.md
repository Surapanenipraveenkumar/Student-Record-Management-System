# Module 2 – Functions, Files & Exception Handling

## Day 6 – Functions

- Functions organize reusable code.
- Parameters pass data into functions.
- Return values send results back.
- Default parameters provide fallback values.

Example:

```python
def add(a, b):
    return a + b
```

## Day 7 – Lambda and List Comprehension

Lambda creates a small anonymous function.

```python
square = lambda x: x * x
```

List comprehension creates lists concisely.

```python
squares = [x * x for x in range(1, 6)]
```

## Day 8 – File Handling

Python supports file operations using `open()` and context managers.

CSV data can be handled using the `csv` module.

JSON data can be handled using the `json` module.

## Day 9 – Exception Handling

Common blocks:

- try
- except
- finally

Exceptions prevent a program from stopping unexpectedly when an error can be handled.

## Day 10 – Student Record Management System

The project implements CRUD:

- Create – Add Student
- Read – View/Search Student
- Update – Modify Student
- Delete – Remove Student

Data is stored in CSV and can be exported to JSON.

## Project Learning Outcome

This project combines Python functions, file handling, CSV/JSON processing, validation and exception handling into one practical application.
