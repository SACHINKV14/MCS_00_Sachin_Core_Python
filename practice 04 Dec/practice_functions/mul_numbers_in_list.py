# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(f'multiplyList {list1} is:{multiplyList(list1)}')
print(f'multiplyList {list2} is:{multiplyList(list2)}')
print("------------------------------------------")

## Python3 program to multiply all values in the
# # list using numpy.prod()
#
# import numpy
#
# list3 = [1, 2, 3]
# list4 = [3, 2, 4]
#
# # using numpy.prod() to get the multiplications
# result3 = numpy.prod(list3)
# result4 = numpy.prod(list4)
# print(f'multiplyList {list3} is:{result3}')
# print(f'multiplyList {list4} is:{result4}')
#
print("-----------------------------------------")

# Python3 program to multiply all values in the
# list using lambda function and reduce()

from functools import reduce

list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)