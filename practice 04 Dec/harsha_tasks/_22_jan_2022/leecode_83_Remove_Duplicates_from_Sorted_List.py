"""
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
class Solution:
    def deleteDuplicates(self, head):
        lst=[]
        for i in head:
            if i not in lst:
                lst.append(i)
        print(lst)

# head = [1, 1, 2]
head = [1,1,2,3,3]
s1=Solution()
s1.deleteDuplicates(head)
