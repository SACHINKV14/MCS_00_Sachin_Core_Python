class Reversestr:
    def rev_str(self,str1):
        rev_str=str1[::-1]
        print(f'Original string is:{str1}')
        print(f'Reversed string is:{rev_str}')

str1=input("enter the string:")
s1=Reversestr()
s1.rev_str(str1)
