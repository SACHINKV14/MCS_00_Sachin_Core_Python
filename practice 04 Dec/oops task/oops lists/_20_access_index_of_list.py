class Lists:
    def lst_index(self,lst1,num):
        if num<=len(lst1):
            print(f'enterd index value in list is:{lst1[num]}')
        else:
            print(f'entered index is not present:')

lst1=[1,2,3,4,5,6,7,8,9]
num=int(input('enter the index to check:'))
l1=Lists()
l1.lst_index(lst1,num)