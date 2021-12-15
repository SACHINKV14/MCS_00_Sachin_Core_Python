class Numb1:
    def even_odd_num(self,num):
        for number in range(1, num+1):
            if(number % 2 == 0):
               # print("{0}".format(number))
               even_numbers.append(number)
            else:
               odd_numbers.append(number)
        return even_numbers,odd_numbers
num = int(input(" Please Enter the Maximum Number : "))
even_numbers=[]
odd_numbers=[]
a1=Numb1()
evens,odds=a1.even_odd_num(num)
print(f' even list: {evens}' )   # confirm the results is ok
print(f' odd list: {odds} ')

