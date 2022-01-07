class Tablenum:
    def num_table(self,num,n1):
        for i in range(1, n1 + 1):
            print(f'{num}*{i}={num * i}')

num=int(input("enter number which u want table:"))
n1=int(input("how many numbers u want:"))
t1=Tablenum()
t1.num_table(num,n1)
print("-----------------------------------------")

class Tablenum1:
    def num_table1(self,num1,n2):
        lst1 = []
        for i in range(1, n2 + 1):
            l1=num1*i
            lst1.append(l1)
        print(f'table of number{num1} is:{lst1}')

num1=int(input("enter number which u want table:"))
n2=int(input("how many numbers u want:"))

t2=Tablenum1()
t2.num_table1(num1,n2)
