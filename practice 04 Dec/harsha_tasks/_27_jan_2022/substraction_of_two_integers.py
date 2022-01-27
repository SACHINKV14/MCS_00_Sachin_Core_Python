class Solution:
    def getSub(self, a: int, b: int) -> int:
        max_num=max(a,b)
        min_num=min(a,b)
        lst=[]
        for i in range(max_num):

            lst.append(1)
        for j in range(min_num):
            lst.remove(1)

        print(len(lst))

a = 1
b = 2
# a = 2
# b = 3
s1=Solution()
s1.getSub(a,b)