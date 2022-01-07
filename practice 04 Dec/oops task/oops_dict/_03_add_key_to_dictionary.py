class Dictaddkey:
    def __init__(self,dict1):
        self.dict1=dict1
    def add_key(self):
        print(f'original dict {self.dict1}')
        self.dict1['b']=2
        print(f'added key to dict{self.dict1}')

dict1={'a':1}
d1=Dictaddkey(dict1)
d1.add_key()
