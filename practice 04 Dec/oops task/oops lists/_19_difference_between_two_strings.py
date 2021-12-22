class Lists:
    def diff_2_lists(self,lst1,lst2):
        lst3=[[i-j] for i,j in zip(lst1,lst2)]
        print(lst3)

lst1=[4,8,9,2,1]
lst2=[1,2,3,4,5]
l1=Lists()
l1.diff_2_lists(lst1,lst2)