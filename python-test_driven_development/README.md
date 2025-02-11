# Python Test-Driven Development

## Project Overview
This repository is dedicated to implementing Python functions with a Test-Driven Development (TDD) approach. It includes functions for basic mathematical operations, string manipulations, and unit testing using `doctest` and `unittest`.

## Background Context
### Important Notice on Intranet Checks for Python Projects
- You must write documentation (module(s) + function(s)) and tests before implementing any code.
- Intranet checks for Python projects will only be released after the first deadline to ensure a focus on TDD.
- Collaboration on test cases is encouraged to cover all possible edge cases, but implementation must be individual.
- Always consider all possible edge cases in your code.

## Learning Objectives
By completing this project, you will learn:
- The importance of writing tests before implementing code.
- How to write interactive tests using `doctest`.
- How to create module and function documentation.
- How to properly structure Python test cases.
- How to identify and handle edge cases effectively.

## Resources
Recommended reading:
- `doctest` — Test interactive Python examples
- `doctest` – Testing through documentation
- `unittest` – Unit Tests in Python

## Requirements
### Python Scripts
- Must be executed on Ubuntu 20.04 LTS using Python 3.8.5.
- Should be properly formatted using `pycodestyle` (version 2.7.*).
- Must have a shebang `#!/usr/bin/python3` as the first line.
- Should end with a new line.
- Should be executable.
- A `README.md` file is mandatory at the root of the project.

### Python Test Cases
- Must be stored inside a `tests` directory.
- Should have a `.txt` extension for `doctest` cases.
- Should be executable using `python3 -m doctest ./tests/*`.
- Functions and modules must have proper documentation.
- `unittest` cases should be Python scripts with `.py` extension.
- Should be executed using `python3 -m unittest tests.<test_file>`.

## Tasks Implemented
### 0. Integers Addition
- Function: `add_integer(a, b=98)`
- Adds two integers and returns the result.
- Raises `TypeError` if the inputs are not integers or floats.
- Converts floats to integers before addition.
- File: `0-add_integer.py`
- Tests: `tests/0-add_integer.txt`

### 1. Matrix Division
- Function: `matrix_divided(matrix, div)`
- Divides all elements of a matrix by a number.
- Raises `TypeError` if the matrix is not a list of lists of integers/floats.
- Raises `TypeError` if rows of the matrix are not of equal size.
- Raises `ZeroDivisionError` if `div` is zero.
- File: `2-matrix_divided.py`
- Tests: `tests/2-matrix_divided.txt`

### 2. Say My Name
- Function: `say_my_name(first_name, last_name="")`
- Prints "My name is <first_name> <last_name>".
- Raises `TypeError` if arguments are not strings.
- File: `3-say_my_name.py`
- Tests: `tests/3-say_my_name.txt`

### 3. Print Square
- Function: `print_square(size)`
- Prints a square of `#` characters of given size.
- Raises `TypeError` if `size` is not an integer.
- Raises `ValueError` if `size` is less than 0.
- File: `4-print_square.py`
- Tests: `tests/4-print_square.txt`

### 4. Text Indentation
- Function: `text_indentation(text)`
- Formats text by adding two new lines after `.`, `?`, and `:`.
- Raises `TypeError` if `text` is not a string.
- File: `5-text_indentation.py`
- Tests: `tests/5-text_indentation.txt`

### 5. Max Integer - Unittest
- Function: `max_integer(list=[])`
- Returns the maximum integer in a list.
- Returns `None` if the list is empty.
- Unit tests created using `unittest`.
- File: `6-max_integer.py`
- Tests: `tests/6-max_integer_test.py`

## How to Run Tests
To run `doctest` tests:
```sh
python3 -m doctest -v ./tests/*
```
To run `unittest` tests:
```sh
python3 -m unittest tests.6-max_integer_test
```

## Author
manuelsantanadev@proton.me