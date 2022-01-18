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
        list1 = []
        count = 0
        for x in range(1, candies+1,3):
            list2 = []
            for y in range(x, x + 3):
                if count < candies :
                    count += y
                    list2.append(y)
                else:
                    break
            if list2:
                list1.append(list2)
        return list1


candies = 10
num_people = 3
s1=Solution()
lst=s1.distributeCandies(candies,num_people)

