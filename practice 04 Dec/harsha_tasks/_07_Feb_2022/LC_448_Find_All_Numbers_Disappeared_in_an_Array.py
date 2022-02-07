"""
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
"""
class Solution:
    def findDisappearedNumbers(self, nums):
        max_n=max(nums)
        min_n=min(nums)
        lst=[x for x in range(min_n,len(nums)+1)]
        lst1=[]
        for i in lst:
            if i not in nums:
                lst1.append(i)

        print(lst1)

# nums = [4, 3, 2, 7, 8, 2, 3, 1]
nums = [1,1]
s1=Solution()
s1.findDisappearedNumbers(nums)