'''
62. Unique Paths
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

m = 3
n = 7

# m=int(input("enter row number:"))
# n=int(input("enter column number:"))

import numpy as np
arr1=np.zeros(shape=(m,n))
#setting 1st row values
for i1 in range(1,m):
    arr1[i1][0]=1
#setting 1st column values
for j1 in range(1,n):
    arr1[0][j1]=1
# print(arr1)

#need to modify here
for i2 in range(1,m):
    for j2 in range(1,n):
        arr1[i2][j2]=arr1[i2][j2-1]+arr1[i2-1][j2]

print(f'number of possible unique paths are {arr1[m-1][n-1]}')

