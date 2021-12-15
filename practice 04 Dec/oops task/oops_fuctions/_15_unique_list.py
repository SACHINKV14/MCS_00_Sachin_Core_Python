class Unique:

    def unique_list(self,lst1):
        unique_lst=list(set(lst1))
        print(f'unique list is:{unique_lst}')

num=int(input("Enter length of list:"))
lst = []
for i in range(num):
    l1 = int(input("Enter number:"))
    lst.append(l1)
print(f'entered list is:{lst}')

a1 = Unique()
a1.unique_list(lst)
