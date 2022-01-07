class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    def display(self):
        print(f'person name is:{self.name}\nperson height is:{self.height}\nperson weight is:{self.weight}')

nam=input("enter the name:")
ht=int(input("enter your height:"))
wt=int(input("enter your weight:"))

sachin=Person(nam,ht,wt)
sachin.display()
