# 1. What is Sorting?
# Sorting means arranging data in a particular order, usually ascending (smallest to largest) or descending (largest to smallest).

# Example:

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)

# Output:
# [1, 2, 3, 5, 8]

# Real-life example: Arranging student marks from lowest to highest or products by price.

# 2. Built-in Sorting in Python

# Python provides two easy ways to sort data.

# A. sort() — sorts the original list.

numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)  # [1, 2, 3, 4]

# B. sorted() — returns a new sorted list without changing the original.

numbers = [4, 1, 3, 2]
result = sorted(numbers)
print(result)   # [1, 2, 3, 4]
print(numbers)  # [4, 1, 3, 2]

# For descending order:

numbers.sort(reverse=True)
print(numbers)  # [4, 3, 2, 1]

# 3. Common Sorting Algorithms
# A sorting algorithm is a step-by-step method for arranging data.

# 1. Bubble Sort

# Compares adjacent elements and swaps them if they are in the wrong order.

# Example: [3, 1, 2] → [1, 3, 2] → [1, 2, 3]

numbers = [5, 3, 8, 1, 2]

n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap adjacent elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)


# Easy to understand, but slow for large datasets.

# 2. Selection Sort

# Finds the smallest element and places it at the beginning of the unsorted section.

# Example: [3, 1, 2] → find 1 → [1, 3, 2] → [1, 2, 3]


numbers = [5, 3, 8, 1, 2]

n = len(numbers)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    # Swap the smallest element into position
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print("Sorted list:", numbers)


# Simple approach with repeated minimum searches.

# 3. Insertion Sort

# Takes one element at a time and inserts it into its correct position in the sorted section.

# Example: [3, 1, 2] → [1, 3, 2] → [1, 2, 3]


numbers = [5, 3, 8, 1, 2]

for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1

    # Shift larger elements one position right
    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    # Insert the element into its correct position
    numbers[j + 1] = key

print("Sorted list:", numbers)


# Useful for small or nearly sorted datasets.

# 4. Merge Sort

# Divides the list into smaller parts, sorts them, and merges them.

# Example: [4, 2, 3, 1] → [4, 2], [3, 1] → [2, 4], [1, 3] → [1, 2, 3, 4]


def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    # Divide the list into two halves
    mid = len(numbers) // 2
    left = merge_sort(numbers[:mid])
    right = merge_sort(numbers[mid:])

    # Merge the sorted halves
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


numbers = [5, 3, 8, 1, 2]
print("Sorted list:", merge_sort(numbers))


# Efficient for large datasets.

# 4. Trace Bubble Sort by Hand

# Suppose the list is [5, 3, 1].
# Step	Comparison	List after step
# 1	Compare 5 and 3; swap	[3, 5, 1]
# 2	Compare 5 and 1; swap	[3, 1, 5]
# 3	Compare 3 and 1; swap	[1, 3, 5]

# Final sorted list: [1, 3, 5]

# Notice that the largest element moves to the end during the first complete pass.

# 5. Built-in Sorting vs Learning an Algorithm

# Built-in sorting	Learning sorting algorithms
# Uses sort() or sorted()	Implements the steps yourself
# Less code and convenient	Helps understand how sorting works
# Best for everyday programming	Useful for interviews and problem-solving
# Python uses Timsort	You may implement Bubble, Selection, or Merge Sort

# Python's built-in sorting is generally the right choice for real applications. Learning algorithms helps you understand their behavior, trade-offs, and efficiency.

# 6. Practice Exercise

numbers = [7, 2, 5, 1, 4]

# Built-in sorting
print(sorted(numbers))

# Trace Bubble Sort manually