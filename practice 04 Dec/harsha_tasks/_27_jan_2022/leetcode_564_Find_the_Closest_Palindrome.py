"""
564. Find the Closest Palindrome
Given a string n representing an integer,
return the closest integer (not including itself),
which is a palindrome. If there is a tie, return the smaller one.
The closest is defined as the absolute difference minimized between two integers.
Example 1:
Input: n = "123"
Output: "121"
Example 2:
Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        lst_s=[]
        lst_g=[]
        b=int(n)
        c=int(n)
        while len(lst_g)!=1:
            b+=1
            bs=str(b)
            if bs==bs[::-1]:
                # print(bs)
                lst_g.append(int(bs))
        while len(lst_s)!=1:
            c-=1
            cs=str(c)
            if cs==cs[::-1]:
                # print(cs)
                lst_s.append(int(cs))
        lst=lst_g+lst_s
        str1=str(min(lst))
        print(str1)

n="123"
# n = "1"
s1=Solution()
s1.nearestPalindromic(n)