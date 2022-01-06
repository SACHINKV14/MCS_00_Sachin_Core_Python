#Append items from iterrable to the end of the array
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,54,90,74])
lst=[1,2,3,4,5]
for i in lst:
    number.append(i)
print(number)
