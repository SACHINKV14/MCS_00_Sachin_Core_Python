"""
387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0
Example 2:
Input: s = "loveleetcode"
Output: 2
Example 3:
Input: s = "aabb"
Output: -1
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1=s
        for i in s1:
            a=s.count(i)
            if a==1:
                print(s.index(i))
                break

        else:
            print("-1")

# s = "leetcode"
# s = "loveleetcode"
s = "aabb"

s1=Solution()
s1.firstUniqChar(s)