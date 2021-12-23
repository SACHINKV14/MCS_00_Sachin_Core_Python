class String:
    def non_repeating_char(self,str1):
        str2=""
        for i in str1.lower():
            if i not in str2:
                str2+=i
        print(f'string without repeating character:{str2}')


str1=input("enter the string:")
s1=String()
s1.non_repeating_char(str1)