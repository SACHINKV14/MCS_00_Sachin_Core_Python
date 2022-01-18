"""
338. Counting Bits
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""
class Solution:
    def bin_count(self,num):
        lst=[]
        for i in range(num+1):
            a=bin(i)
            lst.append(a.count("1"))
        print(lst)

num=int(input("enter number:"))
s1=Solution()
s1.bin_count(num)
