class String:
    def first_repeating_char(self,str1):
        str2=""
        i2=""
        for i in str1.lower():
            if i not in str2:
                str2+=i
            else:
                i2+=i
        print(f'first repeating character is:{i2[0]}')


str1=input("enter the string:")
s1=String()
s1.first_repeating_char(str1)