"""
712. Minimum ASCII Delete Sum for Two Strings
Given two strings s1 and s2,return the lowest ASCII sum of deleted
characters to make two strings equal.
Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str):
        sum=0
        s3 = s2
        s4 = s1
        for i in s1:
            if i not in s3:
                sum += ord(i)
            else:
                s3 = s3.replace(i, "")
        for j in s2:
            if j not in s4:
                sum += ord(j)
            else:
                s4 = s4.replace(j, "")
        print(sum)


# s1 = "delete"
# s2 = "leet"

s1 = "sea"
s2 = "eat"


o1=Solution()
o1.minimumDeleteSum(s1,s2)


