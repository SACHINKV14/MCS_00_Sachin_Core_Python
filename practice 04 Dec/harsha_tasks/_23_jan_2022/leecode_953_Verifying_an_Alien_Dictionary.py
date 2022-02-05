"""
953. Verifying an Alien Dictionary
In an alien language, surprisingly, they also use English lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language.
Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined
as the blank character which is less than any other character (More info).
"""
class Solution:
    def isAlienSorted(self, words, order):
        lst=[x for x in range(1,27)]
        dict1={k:v for k,v in zip(order,lst)}
        lst1=[]
        for word in words:
            lst1.append(dict1[word[0]])
        for i in range(1,len(lst1)):
            if lst1[i-1]>lst1[i]:
                print("false")
                break
        else:
            print("True")



# words = ["hello","leetcode"]
# order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"

s1=Solution()
s1.isAlienSorted(words,order)

