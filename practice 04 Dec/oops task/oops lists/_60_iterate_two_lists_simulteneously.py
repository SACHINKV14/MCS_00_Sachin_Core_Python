class Lists:
    def iterate_2_lists(self,lst1,lst2):
        lst3=[]
        lst3=[[i,j] for i,j in zip(lst1,lst2)]
        print(lst3)
ls1=[1,2,3]
ls2=[4,5,6]
l1=Lists()
l1.iterate_2_lists(ls1,ls2)
