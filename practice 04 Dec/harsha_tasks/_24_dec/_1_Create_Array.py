#Create array of 5 integer and access individual eemets using indexs

import array as arr



class Demo:
    def __init__(self):
        pass
    def access(self,a):
        for i in range(len(a)):
            print(a[i])


d=Demo()
a=arr.array("i",[1,2,3,4,5])
print(type(a))
d.access(a)