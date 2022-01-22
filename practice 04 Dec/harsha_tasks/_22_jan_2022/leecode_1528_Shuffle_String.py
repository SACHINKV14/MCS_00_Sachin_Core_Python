"""
1528. Shuffle String
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position
moves to indices[i] in the shuffled string.
Return the shuffled string.
Example 1:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.
"""
class Solution:
    def restoreString(self, s, indices):
        dict1={x:y for x,y in zip(indices,s)}
        dict2=sorted(dict1.items(),key=lambda x:x[0],reverse=False)
        dict2=dict(dict2)
        # print(dict2)
        lst=[]
        for i in dict2.values():
            lst.append(i)
        str1="".join(lst)
        print(str1)




# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]

s = "abc"
indices = [0,1,2]

s1=Solution()
s1.restoreString(s,indices)
