"""Task

You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones."""

# m,n,p=input().split()
# m = int(m)
# n = int(n)
# p = int(p)

import numpy as np

# print(numpy.zeros((3,3)))
s = (2,2)
print(np.zeros(s))
#Output : [[ 0.  0.]] 

# print numpy.zeros((1,2), dtype = numpy.int) #Type changes to int
# #Output : [[0 0]]