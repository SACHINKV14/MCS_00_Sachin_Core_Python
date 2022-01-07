# multiply all the numbers in a list

try:
    num = int(input("enter length of the list:"))
    lst1 = []
    for i in range(num1):
        l1=int(input("enter number:"))
        lst1.append(l1)
    result = 1
    for x in lst1:
        result = result * x
    print(f'multiply of all numbers in list{lst1} is \"{result}\"')

except NameError:
    print('identifier is not found')




