#GCD of Two Numbers
class Gcd:
    def find_gcd(self,num1,num2):
        num = max(num1, num2)
        print(num)
        lst1 = []
        lst2 = []
        for i in range(1, num1 + 1):
            if num1 % i == 0:
                lst1.append(i)
        print(f'Divisors of {num1} is :{lst1}')
        for j in range(1, num2 + 1):
            if num2 % j == 0:
                lst2.append(j)
        print(f'Divisors of {num2} is :{lst2}')
        lst3 = []

        for k in range(1, num + 1):
            if num1 % k == 0 and num2 % k == 0:
                lst3.append(k)
        print(f'Common Divisors of both numbers:{lst3}')
        GCD = max(lst3)
        print(f'GCD of {num1} and {num2} is \"{GCD}\"')

try:
    n1=int(input("enter first number:"))
    n2=int(input("enter second number:"))
    if n1<=0 or n2<=0:
        raise ValueError
    else:
        n = Gcd()
        n.find_gcd(n1, n2)

except ValueError as v:
    print("enter integers only \'1 or greater than 1\'")



