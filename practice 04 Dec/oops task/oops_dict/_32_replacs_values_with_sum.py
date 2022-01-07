class Sumvalue:
    def __init__(self):
        pass
    def sumdictvalue(self,values):
        total = sum(values)
        print(f'total values of dictionaries is:{total}')
        new_dict={i:total for i in a_dict.keys()}
        print(f'dictionary with sum is:{new_dict}')

a_dict = {"a":1, "b":2, "c": 3}
values = a_dict.values()
d1=Sumvalue()
d1.sumdictvalue(values)