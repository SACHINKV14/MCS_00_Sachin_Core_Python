#how to decorate a method

#decorator func
def check_name(method):
    def inner(name_ref):
        if name_ref.name == 'sachin':
            print(" Hey my name is also same!!!")
        else:
            method(name_ref)
    return inner

class Printing:
    def __init__(self,name):
        self.name=name
    @check_name
    def print_name(self):
         print('entered user name is:',self.name)



p=Printing("dhoni")
p.print_name()