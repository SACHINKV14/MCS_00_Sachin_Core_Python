"""
1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits
and the sum of its digits.
Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str=str(n)
        lst_s=list(n_str)
        sum=0
        prod=1
        for i in lst_s:
            prod=prod*int(i)
            sum+=int(i)
        print(f'Product of digits={prod}')
        print(f'Sum of digits={sum}')
        # print(sum)
        res=prod-sum
        print(f'(Product of digits)-(Sum of digits)={res}')

# n = 234
n=4421
s1=Solution()
s1.subtractProductAndSum(n)