#create array of 5 integers and display and access
import array as arr
number = arr.array('i', [1, 2, 3, 3, 4])
print(number)   #display array
i=int(input("enter index:"))
print('index',i,'element',number[1])   #access element in array