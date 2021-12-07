def even_num(num):
    for number in range(1, num+1):
        if(number % 2 == 0):
           # print("{0}".format(number))
           even_numbers.append(number)
    return even_numbers
num = int(input(" Please Enter the Maximum Number : "))
even_numbers=[]
evens=even_num(num)
print(f' even list: {evens}' )   # confirm the results is ok
