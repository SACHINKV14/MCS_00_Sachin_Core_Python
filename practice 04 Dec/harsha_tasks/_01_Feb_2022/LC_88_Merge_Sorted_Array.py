"""merge Sorted Array
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

"""

class Solution:
    def merge(self, nums1,m,nums2,n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        count = 0
        for ele in nums1:
            if (ele == 0):
                count = count + 1

        if 0 in nums1 and m == 0:
            for j in range(count):
                nums1.remove(0)
        elif 0 in nums1:
            for i in range(m):
                nums1.remove(0)
        nums1.sort(reverse=False)

        return nums1

# nums1 = [1,2,3,0,0,0];m = 3;nums2 = [2,5,6]; n = 3
# nums1 = [1]; m = 1; nums2 = []; n = 0
nums1=[0];m=0;nums2=[1];n=1


s1=Solution()
s1.merge(nums1,m,nums2,n)