# If/Else and For Loops

1. Conditional Statements (if, elif, else)
Conditional statements help a program make decisions based on conditions.

Syntax:

if condition:
    # runs if condition is True
elif another_condition:
    # runs if another condition is True
else:
    # runs if all conditions are False

Example: Check whether a number is positive, negative, or zero.

num = 10

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

Output: Positive number

2. For Loop
A for loop is used to repeat a block of code for each item in a sequence, such as a list or range.

Example 1: Loop through a list

fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)

Output:
Apple
Mango
Banana

Example 2: Using range()
for i in range(1, 6):    
    print(i)

Output:
1
2
3
4
5

Note: range(1, 6) starts at 1 and stops before 6.

3. Combining If/Else with a For Loop
We can use conditions inside loops to make decisions for each item.

scores = [85, 42, 67, 30, 95]

for score in scores:
    if score >= 50:
        print(score, "Pass")
    else:
        print(score, "Fail")

Output:
85 Pass
42 Fail
67 Pass
30 Fail
95 Pass

# 4. Practice Exercise: Score Classifier
Task: Loop through five student records and classify their scores.

students = [
    {"name": "Aman", "score": 85},
    {"name": "Riya", "score": 42},
    {"name": "Rahul", "score": 67},
    {"name": "Priya", "score": 30},
    {"name": "Neha", "score": 95}
]

for student in students:
    score = student["score"]

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 40:
        grade = "C"
    else:
        grade = "Fail"

    print(f"{student['name']}: Score = {score}, Grade = {grade}")

Expected output:
Aman: Score = 85, Grade = A
Riya: Score = 42, Grade = C
Rahul: Score = 67, Grade = B
Priya: Score = 30, Grade = Fail
Neha: Score = 95, Grade = A