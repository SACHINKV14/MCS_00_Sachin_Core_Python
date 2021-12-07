from operator import __mul__


class Sumlist:
    def __init__(self,lst1):
        self.lst1=lst1
    def sum_list(self):
        sum_res=sum(self.lst1)
        print(f'sum of all list elements is :{sum_res}')


num=int(input("Enter number of elements for list :"))
lst1=[]
for i in range(num):
    l1 = int(input('enter number :'))
    lst1.append(l1)
print(f'entered list is :{lst1}')

l1=Sumlist(lst1)
l1.sum_list()


