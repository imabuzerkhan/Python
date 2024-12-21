# A set is a collection of unordered elements.
# Each element in a set is unchangeable and immutable, meaning the elements themselves cannot be altered.
# However, the set itself is mutable, so we can add or remove elements.

# Creating a set of numbers
nums = {1, 2, 3, 5, 6, 7, 8, 9}  # Set of unique numbers
print(nums)  # Output: {1, 2, 3, 5, 6, 7, 8, 9}
print(len(nums))  # Output: 8 (length of the set)
print(type(nums))  # Output: <class 'set'>

# Adding a tuple in a set
tup = {"abuzer", ("khan",)}  # Tuples are immutable, so they can be added to a set
print(tup)  # Output: {'abuzer', ('khan',)}

# We cannot add lists or dictionaries to a set because they are mutable (changeable).

# Removing duplicate values automatically
value = {2, 1, 2, 12, 1, 4, 5, 6, 7, 89, 1, 2, 5, 3}  # Set with duplicate values
print(value)  # Output: {1, 2, 3, 4, 5, 6, 7, 12, 89} (duplicates removed)
print(len(value))  # Output: 9 (unique elements)

# How to create an empty set in Python and methods of sets
collection = set()  # Create an empty set
collection.add(1)  # Add element 1 to the set
collection.add(2)  # Add element 2 to the set
collection.add(3)  # Add element 3 to the set
collection.add(4)  # Add element 4 to the set
collection.remove(1)  # Remove element 1 from the set
collection.clear()  # Remove all elements from the set
collection.pop()  # Remove an arbitrary element (error if the set is empty)

print(collection)  # Output: {} (an empty set after clearing)
