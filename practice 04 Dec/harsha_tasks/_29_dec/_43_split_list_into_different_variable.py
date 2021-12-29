class Lists:
    def split_list(self,lst1):
        a,b,*c = lst1
        print(a)
        print(b)
        print(c)

lst1=['a','b','c','d','e']

l1=Lists()
l1.split_list(lst1)