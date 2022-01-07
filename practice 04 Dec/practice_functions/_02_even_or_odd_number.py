# Python program to check if the input number is odd or even.
# # A number is even if division by 2 gives a remainder of 0.
# # If the remainder is 1, it is an odd number.
#
# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))
#


# Python Program to Print Even Numbers from 1 to N using for loop


def even_num(num):
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
evens,odds=even_num(num)
print(f' even list: {evens}' )   # confirm the results is ok
print(f' odd list: {odds} ')



# # Python Program to Print Even Numbers from 1 to N without using if statement
#
# num = int(input(" Please Enter the Maximum Value : "))
#
# for number in range(2, num+1, 2):
#     print("{0}".format(number))