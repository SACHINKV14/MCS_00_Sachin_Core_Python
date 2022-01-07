#Reverse the order of the items in the array.

#Append a new item to the end of the array.

import array as arr

class Demo:
    def __init__(self):
        pass
    def access(self,a):
        for i in range(len(a)):
            print(a[i])

        print("\n")

    def revv(self,a):
        for i in a[::-1]:
            print(i)

d=Demo()
a=arr.array("i",[1,2,3,4,5])
print(type(a))
d.access(a)
d.revv(a)