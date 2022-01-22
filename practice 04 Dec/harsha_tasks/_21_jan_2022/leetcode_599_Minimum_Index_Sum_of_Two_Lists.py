"""
599. Minimum Index Sum of Two Lists
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.
You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.
Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
"""


class Solution:
    def findRestaurant(self, list1, list2):
        lst3=[]
        for i in list1:
            if i in list2:
                lst3.append(i)
        dict1={}
        for i1 in lst3:
            dict1[i1]=list1.index(i1)+list2.index(i1)
        print(dict1)
        dict2=sorted(dict1.items(),key=lambda x:x[1])
        print(dict2[0])


# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines","Hungry Hunter Steakhouse", "Shogun"]
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]

s1=Solution()
s1.findRestaurant(list1,list2)

