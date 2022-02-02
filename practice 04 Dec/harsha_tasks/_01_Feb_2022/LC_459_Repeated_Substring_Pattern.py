"""
459. Repeated Substring Pattern
Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.
Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:
Input: s = "aba"
Output: false
Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
"""
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lst=[]
        for i in s:
            if i not in lst:
                lst.append(i)
        str1=''.join(lst)
        s1=str1*int(len(s)/len(str1))
        # print(s1)
        if s1==s:
            print('true')
        else:
            print('false')


s = "abab"
# s = "aba"
# s = "abcabcabcabc"
s1=Solution()
s1.repeatedSubstringPattern(s)