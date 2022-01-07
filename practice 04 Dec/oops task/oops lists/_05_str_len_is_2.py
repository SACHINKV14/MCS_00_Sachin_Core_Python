class Lists:
    def str_len_2(self,lst1):
        lst2=[x for x in lst1 if len(str(x))==2]
        print(lst2)

lst1=['sa',12,'23',456,1,'a','#$']
l1=Lists()
l1.str_len_2(lst1)