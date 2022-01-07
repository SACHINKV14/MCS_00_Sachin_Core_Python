class Ballon:
    def __init__(self,color,shape,price):
        self.color=color
        self.shape=shape
        self.price=price
    def display(self):
        print(f'ballon color:{self.color}\n'
              f'ballon shape:{self.shape}\n'
              f'ballon price:{self.price}')


clr=input("enter color:")
shp=input("enter shape:")
prc=int(input("enter price:"))

color_ballon=Ballon(clr,shp,prc)
color_ballon.display()