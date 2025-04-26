# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding and removing elements
my_set.add(6)       # Add an element
my_set.remove(2)    # Remove an element

# Operations
another_set = {4, 5, 6, 7}
union_set = my_set.union(another_set)        # Union of sets
intersection_set = my_set.intersection(another_set)  # Intersection of sets

print(my_set)                # Output: {1, 3, 4, 5, 6}
print(union_set)             # Output: {1, 3, 4, 5, 6, 7}
print(intersection_set)      # Output: {4, 5, 6}


# Creating a frozenset
my_frozenset = frozenset([1, 2, 3, 4, 4, 4, 5])

# You cannot modify a frozenset
# my_frozenset.add(6)  # Error: AttributeError

# Operations (similar to set)
another_frozenset = frozenset([4, 5, 6, 7])
union_frozenset = my_frozenset.union(another_frozenset)       # Union
intersection_frozenset = my_frozenset.intersection(another_frozenset)  # Intersection

print(my_frozenset)                # Output: frozenset({1, 2, 3, 4, 5})
print(union_frozenset)             # Output: frozenset({1, 2, 3, 4, 5, 6, 7})
print(intersection_frozenset)      # Output: frozenset({4, 5})


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = {2,3}
set = set1 - set2
print(set)

print("Difference of set1 and set2 using difference():")
print(set1.difference(set2))
print("Difference of set2 and set1 using difference():")
print(set2.difference(set1))
print("Difference of set1 and set2 using - operator:")
print(set1 - set2)
print("Difference of set2 and set1 using - operator:")
print(set2 - set1)


subset = set3 < set1
print(subset)
#diffrence between set1 and set2 is {1,2,3}
     