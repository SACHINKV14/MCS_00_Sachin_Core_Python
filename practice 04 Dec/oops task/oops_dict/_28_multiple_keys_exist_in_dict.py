class Dictkeymultiple:
    def dict_multiple_keys(self,dict1):
        if len(dict1.keys()) == 0:
            print(f'dictionary have no keys')
        elif len(dict1.keys()) == 1:
            print(f'dictionary have only one key')
        else:
            print(f'dictionary have multiple keys')

# dict1={}
# dict1={'a':1}
dict1={'a':1,'b':2,'c':3}
d1=Dictkeymultiple()
d1.dict_multiple_keys(dict1)
