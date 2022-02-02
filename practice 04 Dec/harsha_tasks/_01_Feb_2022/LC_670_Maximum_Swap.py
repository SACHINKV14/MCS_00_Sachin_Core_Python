"""670. Maximum Swap
You are given an integer num. You can swap two digits at most once to get the maximum valued number.
Return the maximum valued number you can get.
Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap.
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        s1=str(num)
        lst=[]
        lst1=[]
        for i in s1:
            a=int(i)
            lst.append(a)
        # print(lst)
        max_n=max(lst)
        lst1.append(str(max_n))
        lst.remove(max_n)
        for j in lst:
            lst1.append(str(j))
        res=''.join(lst1)
        print(res)

# num = 2736
# num = 9973

s1=Solution()
s1.maximumSwap(num)