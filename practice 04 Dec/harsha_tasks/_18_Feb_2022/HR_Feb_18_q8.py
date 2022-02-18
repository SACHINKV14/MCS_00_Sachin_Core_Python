"""
Transpose
We can generate the transposition of an array using the tool numpy.transpose.
It will not affect the original array, but it will create a new array.
"""

import numpy
n, m = map(int, input("enter n,m:").split())
lista=[list(map(int,input().split())) for i in range(n)]
a=numpy.array(lista)

print(numpy.transpose(a))
print(a.flatten())