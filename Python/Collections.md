1. List — []

A list stores multiple items in order. It is changeable (mutable) and allows duplicate values.

fruits = ["Apple", "Mango", "Banana", "Apple"]print(fruits[0])       # Apple
fruits.append("Orange")
fruits.remove("Mango")
print(fruits)

Output:
Apple
['Apple', 'Banana', 'Apple', 'Orange']


- Ordered: Yes
- Changeable: Yes
- Duplicates: Allowed
Use when: You need a collection that can be updated, such as an inventory list.

2. Tuple — ()
A tuple stores multiple items in order, but it cannot be changed after creation (immutable).

coordinates = (10, 20)
print(coordinates[0])  # 10
print(coordinates[1])  # 20

- Ordered: Yes
- Changeable: No
- Duplicates: Allowed
Use when: Data should remain fixed, such as coordinates or RGB color values.

3. Dictionary — {key: value}
A dictionary stores data as key-value pairs. Keys must be unique, and values can be updated.

item = {    "name": "Laptop",    "price": 50000,    "quantity": 5}
print(item["name"])    # Laptop
item["price"] = 45000
print(item)



Output:
Laptop
{'name': 'Laptop', 'price': 45000, 'quantity': 5}


- Ordered: Yes (insertion order)
- Changeable: Yes
- Duplicate keys: Not allowed
Use when: You need to store related details, such as an item's name, price, and quantity.

4. Set — {} or set()
A set stores unique items and automatically removes duplicates. Sets are unordered and do not support indexing.

numbers = {1, 2, 3, 2, 1}
print(numbers)       # {1, 2, 3}
numbers.add(4)
numbers.discard(2)
print(numbers)       # {1, 3, 4}

- Ordered: No
- Changeable: Yes
- Duplicates: Not allowed
Use when: You need unique values, such as unique employee IDs.

Note: Use set() to create an empty set. {} creates an empty dictionary.
Quick comparison
Feature	List	Tuple	Dictionary	Set
Syntax	[]	()	{key: value}	{}
Ordered	Yes	Yes	Yes	No
Changeable	Yes	No	Yes	Yes
Duplicates	Yes	Yes	Keys: No	No
Access method	Index	Index	Key	Membership

#Practice exercise: Inventory management

This exercise covers your training task: create an inventory list and a dictionary of item details, then iterate and print the results.

# 1. Create an inventory list
inventory = ["Laptop", "Mouse", "Keyboard"]

# 2. Create a dictionary of item details
item_details = {
    "Laptop": {"price": 50000, "quantity": 5},
    "Mouse": {"price": 500, "quantity": 20},
    "Keyboard": {"price": 1000, "quantity": 10}
}

# 3. Print the inventory
print("Inventory Items:")

for item in inventory:
    print(item)

# 4. Print item details
print("\nItem Details:")

for item, details in item_details.items():
    print(f"{item}: Price = ₹{details['price']}, "
          f"Quantity = {details['quantity']}")



Expected output:
Inventory Items:
Laptop
Mouse
Keyboard

Item Details:
Laptop: Price = ₹50000, Quantity = 5
Mouse: Price = ₹500, Quantity = 20
Keyboard: Price = ₹1000, Quantity = 

Remember: List = changeable sequence, Tuple = fixed sequence, Dictionary = key-value pairs, Set = unique values.