class String:
    def n_lower_char(self,str1,num):
        str2 = str1[0:num + 1].lower() + str1[num:len(str1) + 1]
        print(f'string after converting n chars into lower case:{str2}')

str1='AJNNKNLKNLNKMLJKNKNKNKNN'
num=int(input("enter number of chars:"))
s1=String()
s1.n_lower_char(str1,num)