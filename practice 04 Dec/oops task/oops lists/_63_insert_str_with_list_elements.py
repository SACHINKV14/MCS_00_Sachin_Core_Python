class Lists:
    def insert_str(self,lst1):
        lst2=[]
        for i in lst1:
            str1='student'+str(i)
            lst2.append(str1)
        print(lst2)


lst1=[1,2,3,4,5,6,7,8,9]
l1=Lists()
l1.insert_str(lst1)