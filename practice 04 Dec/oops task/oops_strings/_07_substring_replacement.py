class String:
    def substr_replacement(self,str1):
        str1=str1.replace('in','@#',1)
        print(f'string after replacing substring:{str1}')

str1='india is in asia'
s1=String()
s1.substr_replacement(str1)