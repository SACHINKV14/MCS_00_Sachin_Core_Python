"""If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'."""
a=int(input())
lst1=[]
for i in range(a):
    lst1.append(input())

s1=set(lst1)
print(s1)
print(len(s1))
