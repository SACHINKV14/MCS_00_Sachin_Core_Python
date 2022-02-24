"""
floor
The tool floor returns the floor of the input element-wise.
The floor of  is the largest integer  where .
"""
import numpy

a1=list(map(float,input().split()))
arr1=numpy.array(a1)

print(numpy.floor(arr1))
print(numpy.ceil(arr1))
print(numpy.rint(arr1))



print("--------------------------------")
import numpy

numpy.set_printoptions(sign=' ')

array = numpy.array(input().split(),float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))