"""
316. Remove Duplicate Letters
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.
Example 1:
Input: s = "bcabc"
Output: "abc"
Example 2:
Input: s = "cbacdcbc"
Output: "acdb"
"""

import itertools
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lst=[]
        for i in s:
            if i not in lst:
                lst.append(i)
        # print(lst)
        lst1=sorted(lst,reverse=False)
        res1="".join(lst1)
        print(res1)

        #both gives same output
        # perm = itertools.permutations(lst1)
        # res2=[]
        # for i1 in perm:
        #     a=list(i1)
        #     str1="".join(i1)
        #     res2.append(str1)
        # print(res2[0])


s = "bcabc"
# s = "cbacdcbc"


s1=Solution()
s1.removeDuplicateLetters(s)