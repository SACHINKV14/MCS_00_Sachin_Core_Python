"""
1979. Find Greatest Common Divisor of Array
Given an integer array nums,
return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides
both numbers.
Example 1:
Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:
Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:
Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
"""
class Solution:
    def findGCD(self, nums):
        num1=max(nums)
        num2=min(nums)
        lst3=[]
        for k in range(1, num1+ 1):
            if num1 % k == 0 and num2 % k == 0:
                lst3.append(k)
        # print(f'Common Divisors of both numbers:{lst3}')
        GCD = max(lst3)
        print(f'GCD of {num1} and {num2} is \"{GCD}\"')


# nums = [2, 5, 6, 9, 10]
# nums = [7,5,6,8,3]
nums = [3,3]

s1=Solution()
s1.findGCD(nums)