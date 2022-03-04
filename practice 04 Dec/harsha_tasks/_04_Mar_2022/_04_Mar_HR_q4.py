"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character that can be removed to make the string a palindrome. There may be more than one solution, but any will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return the index of a character to remove.
"""


def palindromeIndex(s):
    for i in range(len(s)):
        s1=s.replace(s[i],"")
        if s1=="":
            return -1
            break
        if s1==s1[::-1] and len(s1)==(len(s)-1):
            return i
            break


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)
        print(result)
