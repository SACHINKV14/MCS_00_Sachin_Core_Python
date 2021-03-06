"""
2063. Vowels of All Substrings
Given a string word,
return the sum of the number of vowels ('a', 'e', 'i', 'o', and 'u')
in every substring of word.
A substring is a contiguous (non-empty) sequence of characters within a string.
Note: Due to the large constraints,
the answer may not fit in a signed 32-bit integer. Please be careful during the calculations.
Example 1:
Input: word = "aba"
Output: 6
Explanation:
All possible substrings are: "a", "ab", "aba", "b", "ba", and "a".
- "b" has 0 vowels in it
- "a", "ab", "ba", and "a" have 1 vowel each
- "aba" has 2 vowels in it
Hence, the total sum of vowels = 0 + 1 + 1 + 1 + 1 + 2 = 6.
Example 2:
Input: word = "abc"
Output: 3
Explanation:
All possible substrings are: "a", "ab", "abc", "b", "bc", and "c".
- "a", "ab", and "abc" have 1 vowel each
- "b", "bc", and "c" have 0 vowels each
Hence, the total sum of vowels = 1 + 1 + 1 + 0 + 0 + 0 = 3.

"""
import itertools
class Solution:
    def countVowels(self, word: str) -> int:
        vowels=['a','e','i','o','u']
        lst=[]
        for i in range(len(word)+1):
            for j in range(i+1,len(word)+1):
                lst.append(word[i:j])
        print(lst)
        str1=''.join(lst)
        count=0
        for k in vowels:
            count+=str1.count(k)
        print(count)


# word = "aba"
word = "abc"

s1=Solution()
s1.countVowels(word)