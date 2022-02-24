"""Concatenate

Two or more arrays can be concatenated together using the concatenate
function with a tuple of the arrays to be joined:


import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print numpy.concatenate((array_1, array_2, array_3))
"""
import numpy as np
N,M,P=map(int,input().split())
arr1=np.zeros([N,P],dtype = int)
arr2=np.zeros([M,P],dtype=int)
lst=[]
for i in range(N+M):
    a,b=map(int,input().split())
    lst.extend((a,b))

for i in range(P):
    for j in range(N):
        arr1[i,j]=