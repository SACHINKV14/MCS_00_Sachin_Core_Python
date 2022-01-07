class Lists:
    def sort_elements(self,lst1):
        lst2=[x for x in sorted(lst1,reverse=False)]
        print(lst2)
lst1=[1,9,8,2,7,3,6,4,5]
l1=Lists()
l1.sort_elements(lst1)