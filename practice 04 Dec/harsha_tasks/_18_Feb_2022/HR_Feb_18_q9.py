"""
Task
You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.
Input Format
A single line containing the space separated string  and the integer value .
Constraints
The string contains only UPPERCASE characters.
Output Format
Print the permutations of the string  on separate lines.
"""
import itertools
n, m = input("enter n,m:").split()
m1=int(m)
lst=list(n)
perm=itertools.permutations(lst,m1)
res=[]
for i in perm:
    a=''.join(i)
    if a not in res:
        res.append(a)
res1=sorted(res,reverse=False)
for i1 in res1:
    print(i1)

