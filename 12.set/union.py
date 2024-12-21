# Union of two sets
# The union operation combines all unique elements from both sets.
# It removes any duplicate elements and returns a new set with all unique elements.
set1 = {1, 2, 3, 4, 5, 6, 7, 8}  # First set
set2 = {1, 2, 4, 85, 1, 4, 65432, 13}  # Second set

print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 13, 65432, 85}

# Intersection of two sets
# The intersection operation finds common elements that exist in both sets.
# It returns a new set containing only the elements shared by both sets.
print(set1.intersection(set2))  # Output: {1, 2, 4}
