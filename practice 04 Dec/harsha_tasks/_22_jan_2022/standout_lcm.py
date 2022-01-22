#LCM
'''
LCM(Lowest common Multiple
Smallest non zero common number , which is the multipke of both the numbers
'''
class Lcm:
    def find_lcm(self,num1,num2):
        lst1 = []
        lst2 = []
        for i in range(1, 100):
            lst1.append(num1 * i)
            lst2.append(num2 * i)

        if num1 < num2:
            for i1 in lst1:
                if i1 in lst2:
                    print(f'LCM of two numbers {num1} & {num2} :{i1}')
                    break
        elif num1>num2:
            for i2 in lst2:
                if i2 in lst1:
                    print(f'LCM of two numbers {num1} & {num2} :{i2}')
                    break



try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    if n1<=0 or n2<=0:
        raise ValueError
    else:
        n = Lcm()
        n.find_lcm(n1, n2)

except ValueError as v:
    print("enter integers only \'1 or greater than 1\'")




