class String:
    def len_str(self,str1):
        str2=str1[0:3]
        print(f'original string is:{str1}')
        print(f'first three chars is:{str2}')
        print(f'length of first three chars is:{len(str2)}')

str1='sachin'
s1=String()
s1.len_str(str1)
