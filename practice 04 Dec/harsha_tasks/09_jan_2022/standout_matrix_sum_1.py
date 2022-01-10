lst1=[[1,1],[1,1]]
lst2=[[2,3],[4,5]]

lst3=[i+j for i,j in zip(lst1[0],lst2[0])]
lst4=[i+j for i,j in zip(lst1[1],lst2[1])]
lst5=[lst3,lst4]
for i2 in lst5:
    print(i2)
print(lst5)
print("--------------------------------")
# Adding two matrices

import numpy as np

arr1=np.array([[1,1],[1,1]])
arr2=np.array([[2,3],[4,5]])
arr3=arr1+arr2
print(arr3)

print("------------------------------")

import numpy as np

l1=[]
r=int(input("enter number of rows:"))
c=int(input("enter number of columns:"))
num=r*c
l2=[]
for i1 in range(num):
    b1=int(input("enter the elements rowvice:"))
    l1.append(b1)
for i2 in range(num):
    b2 = int(input("enter the elements for second rowvice:"))
    l2.append(b2)
arrl1=np.array(l1)
newarr1=arrl1.reshape(r,c)
print('new arr1 is',newarr1)
arrl2=np.array(l2)
newarr2=arrl2.reshape(r,c)
print('new arr2 is',newarr2)

newarr3=newarr1+newarr2
print("result array")
print(newarr3)

