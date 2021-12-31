class String:
    def last_str(self,str1):
        lst1=str1.split()
        print(f'last part of string is:{lst1[-1]}')

# str1='india is my country'
str1='india is my,country'
str1=str1.replace(","," ")
s1=String()
s1.last_str(str1)

