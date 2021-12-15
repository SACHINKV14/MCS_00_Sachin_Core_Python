#18 Combine values in python list of dictionaries.
class Dictcombine:
    def dict_combine(self,dict1,dict2):
        dict3 = {y: [x1, x2] for y, x1, x2 in zip(dict1.keys(), dict1.values(), dict2.values())}
        print(f'combining python dictionary values:{dict3}')


dict1 = {'a':1,'b':2,'c':3,'d':4}
dict2 = {'a':11,'b':12,'c':13,'d':14}

a1=Dictcombine()
a1.dict_combine(dict1,dict2)

