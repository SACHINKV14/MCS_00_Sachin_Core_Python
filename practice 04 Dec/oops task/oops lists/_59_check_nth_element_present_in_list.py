class Lists:
    def check_index(self,lst1,num):
        if num<=len(lst1):
            print(f'entered index is present ')
        else:
            print(f'entered index is not present')




lst1=[1,2,3,4,5,6,7,8,9,10]
num=int(input("enter nth index to check:"))
l1=Lists()
l1.check_index(lst1,num)