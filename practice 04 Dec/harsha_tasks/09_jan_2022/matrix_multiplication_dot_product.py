print("------------------------------")
#2*2  Matrix Multiplication
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
arrl2=np.array(l2)
newarr2=arrl2.reshape(c,r)
print('new arr2 is',newarr2)
print('new arr1 is',newarr1)


#creating empty array   `
result = np.zeros(shape=(2,2))

# iterate through rows of X
for i in range(len(newarr1)):
   # iterate through columns of Y
   for j in range(len(newarr2[0])):
       # iterate through rows of Y
       for k in range(len(newarr2)):
           result[i][j] += newarr1[i][k] * newarr2[k][j]

print(result)