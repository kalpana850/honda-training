# 1. What is a Data Structure?
A data structure is a way of storing and organizing data in a computer so that we can access, modify, and manage it efficiently.

Example: A list of employee names, a queue of customer requests, or a stack of browser pages.

# 2. Common Data Structures

1. List (Array)

Stores multiple items in order. Python lists are dynamic, meaning their size can change.

numbers = [10, 20, 30]
print(numbers[0])  # 10
numbers.append(40)

Use case: Storing names, marks, or employee records.

2. Stack (LIFO)

LIFO = Last In, First Out. The last item added is the first item removed.

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack.pop())  # 30

Use case: Undo operations, browser history, function calls.

3. Queue (FIFO)

FIFO = First In, First Out. The first item added is the first item removed.

from collections import deque
queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")
print(queue.popleft())  # A

Use case: Customer service lines, task scheduling, print queues.

4. Dictionary (Hash Map)

Stores data as key-value pairs, allowing fast lookups by key on average.

employee = {"name": "Aman", "age": 22}
print(employee["name"])  # Aman

Use case: Employee details, configuration settings, phone books.

5. Set

Stores unique elements; duplicate values are automatically removed.

nums = {1, 2, 2, 3}
print(nums)  # {1, 2, 3}

Use case: Removing duplicates and checking membership.

6. Trees and Graphs
- Tree: Organizes data hierarchically, like folders on a computer.
- Graph: Represents connections between objects, like cities connected by roads or users connected on social media.

# 3. How are data structures implemented?
Implementation means using programming code to create and operate a data structure.

For example, a stack can be implemented using a Python list:

stack = []

# Push: Add an item
stack.append(10)
stack.append(20)

# Peek: View the top item
print(stack[-1])  # 20

# Pop: Remove the top item
print(stack.pop())  # 20
print(stack)  # [10]

# 4. Stack vs Queue
Feature	Stack	Queue
Principle	LIFO	FIFO
Add operation	append()	append()
Remove operation	pop()	popleft()
Example	Undo operation	Customer waiting line

# 5. Practice Exercise

stack = []
stack.append("Python")
stack.append("Java")
stack.append("C++")
print("Stack:", stack)
removed = stack.pop()
print("Removed:", removed)
print("Updated stack:", stack)

# 6. When is a stack or queue useful?
- Choose a stack when the most recent item must be processed first, such as undoing the latest edit.
- Choose a queue when items should be processed in arrival order, such as handling customer requests.
