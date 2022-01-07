class Wordpalindrome:
    def word_palindrome(self,str1):
        if str1 == str1[::-1]:
            print(f'{str1} is palindrome')
        else:
            print(f'{str1} is not palindrome')

str1=input('Enter a string:')
s1=Wordpalindrome()
s1.word_palindrome(str1)
# print(str1[::-1])
