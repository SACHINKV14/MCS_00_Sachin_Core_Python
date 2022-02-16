"""
73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""
# import numpy as np
# class Solution:
#     def setZeroes(self, matrix) -> None:
#         ar = np.array(matrix)
#         lsti=[];lstj=[]
#         for i in range(len(ar)):
#             for j in range(len(ar[0])):
#                 if ar[i][j]==0:
#                     lsti.append(i)
#                     lstj.append(j)
#         for i1 in lsti:
#             for j1 in range(len(ar)):
#                 ar[i1][j1]=0
#         for i2 in lstj:
#             for j2 in range(len(ar)):
#                 ar[j2][i2]=0
#         print(ar)

class Solution:
    def setZeroes(self, matrix) -> None:
        lsti=[];lstj=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    lsti.append(i)
                    lstj.append(j)
        for i1 in lsti:
            for j1 in range(len(matrix)):
                matrix[i1][j1]=0
        for i2 in lstj:
            for j2 in range(len(matrix)):
                matrix[j2][i2]=0
        print(matrix)



matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

s1=Solution()
s1.setZeroes(matrix)