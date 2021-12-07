class Sumvalue:
    def __init__(self):
        pass
    def sumdictvalue(self,values):
        total = sum(values)
        print(f'total values of dictionaries is:{total}')

a_dict = {"a":1, "b":2, "c": 3}
values = a_dict.values()
d1=Sumvalue()
d1.sumdictvalue(values)