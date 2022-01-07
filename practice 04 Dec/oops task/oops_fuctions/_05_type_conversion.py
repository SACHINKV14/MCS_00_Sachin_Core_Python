class Conversionlists:
    def __init__(self,lst1):
        self.lst1=lst1
    def convert_list_tuple(self):
        tup1=tuple(self.lst1)
        print(f'tuple convert from list:{tup1}')
    def convert_list_set(self):
        set1=set(self.lst1)
        print(f'set convert from list:{set1}')

class Conversionsets:
    def __init__(self,set1):
        self.set1=set1
    def convert_set_tuple(self):
        tup1=tuple(self.set1)
        print(f'tuple convert from set:{tup1}')
    def convert_set_list(self):
        lst1=list(self.set1)
        print(f'list convert from set:{lst1}')

class Conversiontuple:
    def __init__(self,tuple1):
        self.tuple1=tuple1
    def convert_tuple_set(self):
        set1=set(self.tuple1)
        print(f'set convert from tuple:{set1}')
    def convert_tuple_list(self):
        lst1=list(self.tuple1)
        print(f'list convert from tuple:{lst1}')

lst1=[1,2,3,4,5,6,7,8,8]
l1=Conversionlists(lst1)
l1.convert_list_tuple()
l1.convert_list_set()
print("-----------------------------------------------")
set1={1,2,3,4,5,6,7,8,9}
s1=Conversionsets(set1)
s1.convert_set_list()
s1.convert_set_tuple()
print("-----------------------------------------------")
tuple1={1,2,3,4,5,6,7,8,9}
t1=Conversiontuple(tuple1)
t1.convert_tuple_list()
t1.convert_tuple_set()