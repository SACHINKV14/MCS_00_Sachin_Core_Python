import string

class Lists:
    def create_list(self,num):
        lst1=[x for x in range(num)]
        lst2=[x for x in string.ascii_lowercase[0:num]]
        print(f'list 1 is: {lst1}')
        print(f'list 2 is:{lst2}')
num=int(input("enter number of elements :"))
l1=Lists()
l1.create_list(num)

