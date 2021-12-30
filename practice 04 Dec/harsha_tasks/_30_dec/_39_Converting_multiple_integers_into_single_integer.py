class Lists:
    def single_int(self,lst1):
        lst2=[]
        for i in lst1:
            lst2.append(str(i))
        str1="".join(lst2)
        integer=int(str1)
        print(f'single integer from multiple integer is:{integer}')

    def single_int_type_2(self,lst1):
        my_lst_str = ''.join(map(str, lst1))
        print(f'single integer from multiple integer is:{my_lst_str}')

lst1=[8,5,4,6,9,3,9,6]
l1=Lists()
l1.single_int(lst1)
l1.single_int_type_2(lst1)