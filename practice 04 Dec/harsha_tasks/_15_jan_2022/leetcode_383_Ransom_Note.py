"""
383. Ransom Note
Given two stings ransomNote and magazine,
return true if ransomNote can be constructed from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote not in magazine :
            print(False)
        else:
            print(True)


ransomNote = "a"
magazine = "b"

# ransomNote = "aa"
# magazine = "ab"

# ransomNote = "aa"
# magazine = "aab"
s1=Solution()
s1.canConstruct(ransomNote,magazine)
