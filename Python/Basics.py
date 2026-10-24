#1. Python program

# 1. Variables and basic data types
name = "Rahul"        # String
age = 22              # Integer
height = 5.8          # Float
is_student = True     # Boolean

# 2. Output
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# 3. Input from the user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# 4. Simple expressions
next_year_age = user_age + 1
double_age = user_age * 2

# 5. Display results
print("Hello,", user_name)
print("Your age next year will be:", next_year_age)
print("Double your age is:", double_age)


#Practice Exercises:


# Accept a name and two numbers
name = input("Enter your name: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate results
total = num1 + num2
difference = num1 - num2
product = num1 * num2

# Print formatted results
print("\n----- Calculation Results -----")
print(f"Hello, {name}!")
print(f"First number: {num1:g}")
print(f"Second number: {num2:g}")
print(f"Sum: {total:g}")
print(f"Difference: {difference:g}")
print(f"Product: {product:g}")
print("--------------------------------")
