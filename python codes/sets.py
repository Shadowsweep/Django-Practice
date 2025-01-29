# Define two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union - Combines elements from both sets
union_set = set1 | set2  # OR: set1.union(set2)
print("Union:", union_set)

# Intersection - Common elements in both sets
intersection_set = set1 & set2  # OR: set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference - Elements in set1 but not in set2
difference_set = set1 - set2  # OR: set1.difference(set2)
print("Difference (set1 - set2):", difference_set)

# Symmetric Difference - Elements in either set, but not both
symmetric_diff_set = set1 ^ set2  # OR: set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_diff_set)
