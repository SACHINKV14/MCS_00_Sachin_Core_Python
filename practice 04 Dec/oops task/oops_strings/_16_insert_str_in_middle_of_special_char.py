class String:
    def insert_special_char(self,str1):
        special_char='@&**(*(^&%^'
        str2=special_char[0:5]+str1+special_char[5:]
        print(f'string in between special chars is:{str2}')
str1='india'
s1=String()
s1.insert_special_char(str1)