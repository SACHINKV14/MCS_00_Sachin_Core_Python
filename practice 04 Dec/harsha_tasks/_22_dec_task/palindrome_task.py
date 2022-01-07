'''214. Shortest Palindrome
Hard

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.'''

class Solution:
    def palindrome_str(self,str1):
        if str1 == str1[::-1]:
            print(f'entered str \"{str1}\" is a palindrome')
        else:
            str2 = str1[-1:0:-1] + str1
            print(f'original string:{str1}\n'
                  f'string converted to palindrome:{str2}')


str1=input("enter the string:")
s1=Solution()
s1.palindrome_str(str1)