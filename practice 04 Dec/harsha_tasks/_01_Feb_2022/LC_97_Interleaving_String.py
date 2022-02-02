"""
97. Interleaving String
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        for i in s1:
            if i in s3:
                s1=s1.replace(i," ",1)
                s3=s3.replace(i," ",1)

        for i in s2:
            if i in s3:
                s2 = s2.replace(i, " ", 1)
                s3 = s3.replace(i, " ", 1)
        s3=s3.replace(" ","")
        s1=s1.replace(" ","")
        s2=s2.replace(" ","")
        if len(s1)==0 and len(s2)==0 and len(s3)==0:
            print(True)
        else:
            print(False)

# s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"

s1 = ""; s2 = "dca"; s3 = "dac"

o1=Solution()
o1.isInterleave(s1, s2, s3)

