
print("------------------------------")
#To multiply a matrix by a single number is easy:
import numpy as np

l1=[]
r=int(input("enter number of rows:"))
c=int(input("enter number of columns:"))
num=r*c
l2=[]
for i1 in range(num):
    b1=int(input("enter the elements rowvice:"))
    l1.append(b1)
a=int(input("enter element to multiply with matrix:"))
arrl1=np.array(l1)
newarr1=arrl1.reshape(r,c)
print('new arr1 is',newarr1)
newarr3=a*newarr1
print("result array")
print(newarr3)