class String:
    def replace_string(self,str1):
        str1=str1.replace('a','*',1)
        print(str1)

str1='sachin is good hardworker'
s1=String()
s1.replace_string(str1)