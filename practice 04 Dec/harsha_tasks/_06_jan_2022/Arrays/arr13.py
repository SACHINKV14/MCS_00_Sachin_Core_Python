# Convert an array to an ordinary list with the same items.
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,54,90,74])
lst=[]
for i in number:
    lst.append(i)
print(lst)