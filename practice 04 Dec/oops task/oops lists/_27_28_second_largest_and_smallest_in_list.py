class Largestsmallestnum:
    def __init__(self,lst1):
        self.lst1=lst1
    def lar_num(self):
        print(f'largest num in list is:{sorted(self.lst1,reverse=False)[-2]}')
    def smal_num(self):
        print(f'smallest num in list is:{sorted(self.lst1,reverse=False)[1]}')

num=int(input("Enter number of elements:"))
lst1=[]
for i in range(num):
    l1=int(input("enter number:"))
    lst1.append(l1)
print(f'Entered list is {lst1}')
l1=Largestsmallestnum(lst1)
l1.lar_num()
l1.smal_num()