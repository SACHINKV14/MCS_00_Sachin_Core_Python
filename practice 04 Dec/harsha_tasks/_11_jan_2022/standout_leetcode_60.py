'''
60. Permutation Sequence
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
'''
import itertools
n=int(input("enter the number of element:"))
lst=[]
for i in range(1,n+1):
    lst.append(str(i))
perm=itertools.permutations(lst)
lst1=[]
for i1 in perm:
    i1=list(i1)
    lst1.append("".join(i1))
# print(lst1)
k=int(input("enter the element to find:"))
print(lst1[k-1])