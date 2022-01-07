'''The copy() method returns a shallow copy of the set in python. If we use “=” to copy a set to another set,
when we modify in the copied set, the changes are also reflected in the original set.'''


set1 = {1, 2, 3, 4}

# function to copy the set
set2 = set1.copy()

# prints the copied set
print(set2)

print("------------------------------------------")