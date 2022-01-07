#type 1
class String:
    def add_identation(self,var,num):
        for i in range(num):
            print(" ", end="")
        else:
            print(var)
        print(" "*num+var)
var="""sachin is 
very good
boy
"""
s1=String()
num=int(input("enter number of indentation:"))
s1.add_identation(var,num)
print("--------------------------------------")
#type 2
class String:
    def add_identation(self,var,num):
        print(" "*num+var)
var="""sachin is 
very good
boy
"""
s1=String()
num=int(input("enter number of indentation:"))
s1.add_identation(var,num)