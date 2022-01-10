import numpy as np
# matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix = np.array([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
m,n=matrix.shape
print('original matrix','\n',matrix)

#transposing matrix
matrix=matrix.transpose()
print('matrix after transpose','\n',matrix)