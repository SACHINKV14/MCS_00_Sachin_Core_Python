"""
Example 1:
Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Example 2:
Input: candies = 10, num_people = 3
Output: [5,2,3]
"""

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        lst=[]
        a=0
        while sum(lst)<candies:
            a+=1
            lst.append(a)
        print(lst)
        dict1={}
        for i in range(1,num_people+1):
            dict1[i]=sum(lst[i-1::num_people])
        res=list(dict1.values())
        print(res)


# candies = 10
# num_people = 3

candies = 7
num_people = 4

s1=Solution()
lst=s1.distributeCandies(candies,num_people)