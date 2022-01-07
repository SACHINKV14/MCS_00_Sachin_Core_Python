# A Sample class with init method
class person:
    # init method or constructor
    def __init__(self,n,c):
        self.name=n
        self.capital=c
    # Creating different objects
    def say_hi(self):
        print("hello!My name is",self.name)
        print("my capitsl is ",self.capital)


p2=person('india','delhi')
p3=person('karnataka','bangalore')

p2.say_hi()
p3.say_hi()