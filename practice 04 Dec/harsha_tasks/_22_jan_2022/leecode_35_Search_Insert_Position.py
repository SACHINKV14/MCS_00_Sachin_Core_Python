"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [1, 3, 5, 6], target = 5
Output: 2
Example 2:
Input: nums = [1, 3, 5, 6], target = 2
Output: 1
Example 3:
Input: nums = [1, 3, 5, 6], target = 7
Output: 4
"""
class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            print(nums.index(target))
        else:
            lst=[]
            for i in nums:
                if i<target:
                    lst.append(i)
            a=max(lst)
            print(nums.index(a)+1)

# nums = [1, 3, 5, 6]
# target = 5

# nums = [1, 3, 5, 6]
# target = 2

nums = [1, 3, 5, 6]
target = 7

s1=Solution()
s1.searchInsert(nums,target)