# Goal: Learn how to test Python functions and make scripts reusable using command-line arguments.

1. What is Unit Testing?
Unit testing means testing a small part of a program, such as a single function, to check whether it works correctly.

Python has a built-in unittest module for writing tests.

Example function:
def add(a, b):
    return a + b

A unit test checks whether add(2, 3) returns 5.

2. What is argparse?
argparse is a built-in Python module that allows users to pass inputs to a program through the terminal.

Without argparse, you might need to edit your code to change an input. With it, you can supply different values when running the program.

For example:
python calculator.py 10 20

Here, 10 and 20 are command-line arguments.

3. Practical Example: Function + Two Unit Tests + CLI
Create a file named calculator.py.


import argparse

def add(a, b):
    return a + b

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add two numbers"
    )

    parser.add_argument("num1", type=float)
    parser.add_argument("num2", type=float)

    args = parser.parse_args()

    result = add(args.num1, args.num2)
    print("Result:", result)


This script adds two numbers supplied through the terminal.

4. Write Two Unit Tests

Create another file named test_calculator.py in the same folder.

import unit test
from calculator import add

class TestAddition(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == "__main__":
    unittest.main()

Understand the important parts
- unittest.TestCase: Base class for your test cases.
- assertEqual(actual, expected): Checks whether two values are equal.
- test_positive_numbers(): Tests addition with positive values.
- test_negative_numbers(): Tests addition with negative values.

5. Run the Unit Tests in VS Code
Open the terminal in the folder containing both files and run:
>>python -m unittest -v test_calculator.py

Expected output:
test_negative_numbers ... ok
test_positive_numbers ... ok

Ran 2 tests

OK

This means both tests passed.
6. Run the Script Using Command-Line Arguments
In the same terminal, run:
python calculator.py 10 20

Expected output:
Result: 30.0

Try another input:
python calculator.py 5 7

Output:
Result: 12.0

You can change the numbers without editing the Python code.