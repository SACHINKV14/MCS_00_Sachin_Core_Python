class Dictgen:
    def dict_gen(self,num):
        dict1={x: x*x for x in range(1, 15)}
        print(dict1)
num=15
d1=Dictgen()
d1.dict_gen(num)