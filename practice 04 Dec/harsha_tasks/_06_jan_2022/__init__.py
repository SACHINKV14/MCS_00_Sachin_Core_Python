class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
n=5
s1=Solution()
a=s1.arrangeCoins(n)
print(a)