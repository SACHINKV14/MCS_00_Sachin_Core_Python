#Append items from a specified list.
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,54,90,74])
lst=[8,5,4,6,9,3]
for i in lst:
    number.append(i)
print(number)