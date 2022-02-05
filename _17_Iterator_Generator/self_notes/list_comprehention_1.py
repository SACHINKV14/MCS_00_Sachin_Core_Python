
# Nested list comprehension
#even odd in sublist
lst = [[j for j in range(10+1) if j%2==0 if j!=0],[j1 for j1 in range(10) if j1%2!=0]]
print(lst)
lst1=[]
print("-----------------------------------")
# Nested list comprehension
lst3 = [[j for j in range(5)] for i in range(5)]
print(lst3)
print("-----------------------------------")
# 2-D List
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Nested List Comprehension to flatten a given 2-D matrix
flatten_matrix1 = [val for val in matrix]
print(flatten_matrix1)
flatten_matrix2 = [val for sublist in matrix for val in sublist]
print(flatten_matrix2)

print("-----------------------------------")
