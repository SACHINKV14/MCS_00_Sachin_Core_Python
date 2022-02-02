"""
461. Hamming Distance
The Hamming distance between two integers is
the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.
Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:
Input: x = 3, y = 1
Output: 1
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x1=bin(x)
        y1=bin(y)
        x1=x1[2::]
        y1=y1[2::]
        max_n=max(len(x1),len(y1))
        min_n=min(len(x1),len(y1))
        lst1=[x1[::-1]]
        if len(x1)!=max_n:
           for i in range(max_n)
            lst1.append('0')
        print(x1)
        print(lst1)





x = 1;y = 4
s1=Solution()
s1.hammingDistance(x,y)