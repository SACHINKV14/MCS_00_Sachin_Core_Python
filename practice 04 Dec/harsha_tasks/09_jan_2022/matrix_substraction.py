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

newarr3=newarr1-newarr2
print("result array")
print(newarr3)