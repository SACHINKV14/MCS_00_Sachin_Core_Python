"""
Task

You are given a space separated list of nine integers. Your task is to convert this list into a X NumPy array.
import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array,(3,2))

#Output
[[1 2]
[3 4]
[5 6]]
"""
import numpy
print(numpy.array(input().split(), int).reshape(3, 3))
