class String:
    def remove_dupliacte_char(self,str1):
        str2=""
        for i in str1.lower():
            if i not in str2:
                str2+=i
        print(f'string after  removing duplicate character:{str2}')

str1=input("enter the string:")
s1=String()
s1.remove_dupliacte_char(str1)