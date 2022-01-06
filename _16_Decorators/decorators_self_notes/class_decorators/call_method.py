class Printing:
    def __init__(self,name):
        self.name=name

    def __call__(self):
        print("entered user name is:",self.name)
p=Printing("sachin")
p( )
