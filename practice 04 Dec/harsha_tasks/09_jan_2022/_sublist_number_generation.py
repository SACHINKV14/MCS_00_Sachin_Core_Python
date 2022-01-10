lst3=[]
lst4=[]
num=int(input("enter number of elements:"))
num1=int(input("enter number elements in sublist"))
num2=num//num1
print(num2)
for j in range(1,num+1):
    lst3.append(j)
# print(lst3)
a=0
b=5
for i in range(1,num2+1):
    lst4.append(lst3[a:a+5:1])
    a+=5
print(lst4)
