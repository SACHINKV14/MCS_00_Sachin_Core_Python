"""70. Climbing Stairs
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = 1
        f2 = 2
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            count = 2
            f3 = 0
            while (count != n):
                f3 = f1 + f2
                f1 = f2
                f2 = f3
                count += 1
            return f3


# n = 2
n=11
s1=Solution()
a=s1.climbStairs(n)
print(a)

