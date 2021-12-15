class Numeven:

    def even_num(self,num):
        for number in range(1, num+1):
            if(number % 2 == 0):
           # print("{0}".format(number))
                even_numbers.append(number)
        return even_numbers
num = int(input(" Please Enter the Maximum Number : "))
even_numbers=[]
a1=Numeven()
evens=a1.even_num(num)
print(f' even list: {evens}' )   # confirm the results is ok
