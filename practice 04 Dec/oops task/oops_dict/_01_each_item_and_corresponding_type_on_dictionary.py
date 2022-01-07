class Dicttype:
    def __init__(self,lst1):
        self.lst1=lst1
    def dict_type(self):
        new_dict = {self.lst1[i]: type(self.lst1[i]) for i in range(len(self.lst1))}
        print(new_dict)

lst1=['s',1,2.5,(3,4),3+4j]
d1=Dicttype(lst1)
d1.dict_type()


