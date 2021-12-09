#multiply all the numbers in a list

try:
    num = int(input("enter length of the list:"))
    lst1 = []
    for i in range(num):
        l1=int(input("enter number:"))
        lst1.append(l1)
        res=sum(lst1)
    print(f'sum of all numbers in list{lst1} is \"{res}\"')

except ValueError:
    print('enter integer numbers')





