# Get the number of occurrences of a specified element in an array
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,1,2,1,2,1,2,54,90,74])
num=int(input('enter number to count:'))
print(f'count of {num} is {number.count(num)}')