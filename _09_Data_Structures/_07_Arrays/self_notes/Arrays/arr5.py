# Get the current memory address and the length in elements of the buffer used to hold an arrays? contents and also find the size
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4,88,9,8,54,90,74])
print(number.buffer_info())   #prints address and size