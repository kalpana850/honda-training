# Logging — Make Programs Observable

# 1. What is logging?
# Logging means recording important events that happen while a program runs, such as success messages, warnings, and errors.

# Instead of relying only on print(), Python provides the built-in logging module.

# 2. print() vs logging
# print()	logging
# Displays messages on the screen	Records meaningful program events
# No built-in severity levels	Supports INFO, WARNING, ERROR, etc.
# Mainly useful for simple output	Useful for debugging and monitoring

# 3. Important logging levels
# Level	Purpose	Example
# DEBUG	Detailed debugging information	Variable value
# INFO	Normal program activity	Program started successfully
# WARNING	Something unexpected	Input may be missing
# ERROR	An operation failed	File could not be opened
# CRITICAL	A serious failure	Application cannot continue

# 4. Practical example in Python

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.info("Division operation started")

    try:
        result = a / b
        logging.info("Division completed successfully")
        print("Result:", result)

    except ZeroDivisionError:
        logging.error("Division failed: Cannot divide by zero")

divide(10, 2)
divide(10, 0)

# 5. What does logging.basicConfig() do?
# - level=logging.INFO: Displays INFO messages and higher-severity messages, such as WARNING and ERROR.
# - format=...: Specifies how each log message appears.
# - logging.info(): Records a normal event.
# - logging.error(): Records a failure.
# Note: Logging levels help filter messages. With INFO configured, DEBUG messages are not displayed.

# 6. Practice task
# Update your previous Python script by adding:
# - logging.info() when the script starts.
# - logging.info() when the task completes successfully.
# - logging.error() when an operation fails.


import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

def calculate_sum():
    logging.info("Program started")

    try:
        name = input("Enter your name: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 + num2

        print(f"Hello {name}, the sum is {result}")
        logging.info("Task completed successfully")

    except ValueError:
        logging.error("Operation failed: Please enter valid numbers")

    except Exception:
        logging.error("An unexpected error occurred")

calculate_sum()
