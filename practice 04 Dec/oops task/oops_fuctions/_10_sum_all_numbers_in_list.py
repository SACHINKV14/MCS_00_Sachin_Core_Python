class Sumlst:

    def sum_list(self,lst):
        print(f'sum of all elemnets in lists is:{sum(lst)}')


num=int(input("enter length of list:"))
lst=[]
for i in range(num):
    l1=int(input("enter the number:"))
    lst.append(l1)
print(f'Entered list is:{lst}')

o1=Sumlst()
o1.sum_list(lst)


