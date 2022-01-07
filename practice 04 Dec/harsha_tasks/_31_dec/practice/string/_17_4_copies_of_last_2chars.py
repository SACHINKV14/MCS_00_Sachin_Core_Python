#4 Copies of last 2 chars
class String:
    def copy_str(self,str1):
        b=str1[-2:]
        print(str1+b*4)

str1='sachin'
s1=String()
s1.copy_str(str1)