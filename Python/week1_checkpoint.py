# Clean Python code


def get_numbers():
    """Accept two numbers from the user."""
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    return first_number, second_number


def calculate_results(first_number, second_number):
    """Calculate basic arithmetic results."""
    return {
        "Sum": first_number + second_number,
        "Difference": first_number - second_number,
        "Product": first_number * second_number
    }


def main():
    user_name = input("Enter your name: ")
    first_number, second_number = get_numbers()

    results = calculate_results(first_number, second_number)

    print(f"\nHello, {user_name}!")
    for operation, result in results.items():
        print(f"{operation}: {result:g}")


if __name__ == "__main__":
    main()

# What is shallow copy and deep copy?

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 99

print(shallow)  # [[99, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]

# - Shallow copy: Creates a new outer collection but shares nested objects with the original.
# - Deep copy: Creates a separate copy of nested objects too.
# These concepts matter when working with nested lists or dictionaries and we want to avoid unintended changes.