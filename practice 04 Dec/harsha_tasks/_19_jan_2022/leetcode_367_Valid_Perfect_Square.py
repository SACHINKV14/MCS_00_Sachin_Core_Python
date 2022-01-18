"""
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
Example 1:
Input: num = 16
Output: true
Example 2:
Input: num = 14
Output: false
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lst = [x * x for x in range(1, 100)]
        if num in lst:
            print("True")
        else:
            print("False")

num=14
s1=Solution()
s1.isPerfectSquare(num)

