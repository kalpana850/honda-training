# While Loops and Functions

1. While Loop
A while loop repeatedly executes a block of code as long as a condition is True.

Syntax:
while condition:
    # code to execute

Example: Print numbers from 1 to 5

i = 1

while i <= 5:
    print(i)
    i += 1

Output:
1
2
3
4
5

>> Important: Update the variable inside the loop to avoid an infinite loop.

2. Input Validation Using a While Loop
Input validation ensures the user enters acceptable data.

score = int(input("Enter score (0-100): "))

while score < 0 or score > 100:
    print("Invalid score! Try again.")
    score = int(input("Enter score (0-100): "))

print("Valid score:", score)

-The loop continues until the score is between 0 and 100.

3. Functions in Python
A function is a reusable block of code that performs a specific task. Functions reduce repetition and make code easier to maintain.

Syntax:
def function_name(parameters):
    # code
    return result

Example: Calculate the sum of two numbers

def add(a, b):
    return a + b

result = add(10, 20)
print(result)

Output: 30
- def defines a function.
- a, b are parameters.
- return sends the result back to the caller.
- add(10, 20) calls the function.

# 4. Practice: Refactor Yesterday's Script
This example uses two functions and a while loop to validate the score input.

# Function 1: Get a valid score
def get_score():
    while True:
        try:
            score = int(input("Enter score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid whole number.")


# Function 2: Classify the score
def classify_score(score):
    if score >= 80:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 40:
        return "C"
    else:
        return "Fail"


# Main program
name = input("Enter student name: ")
score = get_score()
grade = classify_score(score)

print(f"{name}: Score = {score}, Grade = {grade}")

Sample output:
Enter student name: Aman
Enter score (0-100): 120
Score must be between 0 and 100.
Enter score (0-100): abc
Please enter a valid whole number.
Enter score (0-100): 85
Aman: Score = 85, Grade = A