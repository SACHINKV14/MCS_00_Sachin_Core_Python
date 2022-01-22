"""
1160. Find Words That Can Be Formed by Characters
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars
(each character can only be used once).
Return the sum of lengths of all good strings in words.
Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""
class Solution:
    def countCharacters(self, words, chars):
        lst=[]
        for word in words:
            for i in word:
                if i not in chars:
                    break
            else:
                lst.append(word)
        print(lst)
        str1="".join(lst)
        print(len(str1))

# words = ["cat","bt","hat","tree"]
# chars = "atach"

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

s1=Solution()
s1.countCharacters(words,chars)