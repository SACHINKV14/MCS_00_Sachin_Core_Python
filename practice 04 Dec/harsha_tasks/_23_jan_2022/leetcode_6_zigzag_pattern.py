"""
6. Zigzag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        for i in range(numRows):
            if i==0 or i==numRows-1:
                print(s[i:len(s):numRows+2])    #to get leetr by interval 6



s = "PAYPALISHIRING"
numRows = 4
s1 = Solution()
s1.convert(s, numRows)