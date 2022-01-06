#Remove a specified item using the index from an array.
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,54,90,74])
number.pop(3)   #removing element with index
print(number)