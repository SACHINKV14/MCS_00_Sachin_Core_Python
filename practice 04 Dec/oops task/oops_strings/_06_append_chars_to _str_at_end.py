class String:
    def append_char_end(self,str1):
        str1=str1+str1[-1]*6
        print(str1)
str1='google'
s1=String()
s1.append_char_end(str1)