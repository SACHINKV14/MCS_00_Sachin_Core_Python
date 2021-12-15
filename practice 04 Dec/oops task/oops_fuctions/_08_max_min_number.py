# Python program to find the largest
# number among the three numbers
class Numb1:
    def maximum(self,lst1):
       print(f'max number is: {max(lst1)}')
       print(f'min number is: {min(lst1)}')

num = int(input("Enter length of Number:"))
lst1=[]
for i in range(num):
    l1=int(input("enter number:"))
    lst1.append(l1)

a1=Numb1()
a1.maximum(lst1)
