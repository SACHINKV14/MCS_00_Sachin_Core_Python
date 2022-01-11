'''
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

'''

import math

a=2
b=-2
res=1
if b>0:
    for i in range(1,b+1):
        res=res*a
    print(res)
else:
    b =(-1)*(b)
    # print(b)
    for i in range(1,b+1):
        d=res*a
    res=1/d
    print(res)