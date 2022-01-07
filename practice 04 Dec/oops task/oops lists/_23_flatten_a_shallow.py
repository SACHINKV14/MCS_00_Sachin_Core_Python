class Lists:
    def shallow_lists(self,lst1):
        lst2=[]
        for i in lst1:
            for j in i:
                lst2.append(j)
        print(f'original list is:{lst1}')
        print(f'shallowed list is:{lst2} ')

lst1=[[1,2],[1,9],[50,100]]
l1=Lists()
l1.shallow_lists(lst1)