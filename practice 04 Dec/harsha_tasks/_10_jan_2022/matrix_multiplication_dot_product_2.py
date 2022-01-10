print("------------------------------")
#2*2  Matrix Multiplication
import numpy as np


r1=int(input("enter number of rows for first matrix:"))
c1=int(input("enter number of columns for first matrix:"))
num1=r1*c1

l1=[]
for i1 in range(num1):
    b1=int(input("enter the elements for first matrix rowvice:"))
    l1.append(b1)

l2=[]
r2=int(input("enter number of rows for second matrix:"))
c2=int(input("enter number of columns for second matrix:"))
num2=r2*c2
for i2 in range(num2):
    b2 = int(input("enter the elements for second matrix rowvice:"))
    l2.append(b2)
arrl1=np.array(l1)
newarr1=arrl1.reshape(r1,c1)
arrl2=np.array(l2)
newarr2=arrl2.reshape(r2,c2)
print('new arr2 is',newarr2)
print('new arr1 is',newarr1)

if c1==r2:
    #creating empty array   `
    result = np.zeros(shape=(r1,c2))
    print(result)

    # iterate through rows of X
    for i in range(len(newarr1)):
       # iterate through columns of Y
       for j in range(len(newarr2[0])):
           # iterate through rows of Y
           for k in range(len(newarr2)):   #
               result[i][j] += newarr1[i][k] * newarr2[k][j]

    print(result)
else:
    print("Multiplication not possible")