"""
500. Keyboard Row
Given an array of strings words,
return the words that can be typed using letters of the alphabet
on only one row of American keyboard like the image below.
In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""
class Solution:
    def findWords(self, words):
        keyboard=["qwertyuiop","asdfghjkl","zxcvbnm"]
        lst1=[]
        for word in words:
            print(word)
            for i in word:
                if i not in keyboard[0]:
                    break
            else:
                lst1.append(word)
        print(lst1)

        lst2 = []
        for word in words:
            print(word)
            for i in word:
                if i not in keyboard[1]:
                    break
            else:
                lst2.append(word)
        print(lst2)


words = ["Hello","Alaska","Dad","Peace"]

s1=Solution()
s1.findWords(words)