#type 1
class String:
    def str_width(self,str1):
        for i in range(50):
            print(" ",end="")
        else:
            print(str1)

str1="sachin"
s1=String()
s1.str_width(str1)
print("--------------")
#type 2
class String2():
    def str_width2(self,str2):
        print(format(str2,">50"))

str2="sachin"
s2=String2()
s2.str_width2(str2)
print("--------------")
#type3
num=int(input("enter number of indentation:"))
print(" "*num+str2)
