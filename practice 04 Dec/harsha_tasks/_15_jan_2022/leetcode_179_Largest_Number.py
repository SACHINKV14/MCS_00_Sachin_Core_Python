"""
179. Largest Number
Given a list of non-negative integers nums,
arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"
Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

class Solution:
    def largestNumber(self, nums):
        lst=[]
        for i in nums:
            a=str(i)
            lst.append(a)
        lst1 = sorted(lst, reverse=True)
        str1="".join(lst1)
        print(str1)

# nums = [10,2]
nums = [3,30,34,5,9]
s1=Solution()
s1.largestNumber(nums)