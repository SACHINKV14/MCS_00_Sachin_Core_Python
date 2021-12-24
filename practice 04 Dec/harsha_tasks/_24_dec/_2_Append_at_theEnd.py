#Append a new item to the end of the array.

import array as arr

class Demo:
    def __init__(self):
        pass
    def access(self,a):
        for i in range(len(a)):
            print(a[i])
    def addd(self,a):
        a1=int(input("enter the new value"))
        a.append(a1)


d=Demo()
a=arr.array("i",[1,2,3,4,5])
print(type(a))
d.access(a)
d.addd(a)
print(a)