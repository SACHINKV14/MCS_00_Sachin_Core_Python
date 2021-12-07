class ballon:
    def __init__(self,s,c,r):   #constructor
        self.shape=s
        self.color=c
        self.radius=r


    #method has function   state has attributes
    def ballon_property(self):
        print("ballon properties",self.shape,self.color,self.radius)

b1=ballon('oval','red',5)
print(b1.shape)
print(b1.color)
b1.ballon_property()