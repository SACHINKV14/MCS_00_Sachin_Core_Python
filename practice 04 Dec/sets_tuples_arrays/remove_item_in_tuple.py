'''Tuples in python are immutable. If you want to remove items out of a Python tuple,
you can use index slicing to leave out a particular index. For example,
'''
#can use index slicing to leave out a particular index. For example,
a = (1, 2, 3, 4, 5)
b = a[:2] + a[3:]
print(b)

print("------------------------")
a = (1, 2, 3, 4, 5)
ls_a = list(a)
del ls_a[2]

b = tuple(ls_a)
print(b)