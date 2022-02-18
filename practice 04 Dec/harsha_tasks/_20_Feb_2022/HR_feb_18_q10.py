"""
Task
You are given a string .
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.
Input Format
A single line containing the string  and integer value  separated by a space.
Constraints
The string contains only UPPERCASE characters.
Output Format
Print the different combinations of string  on separate lines.

"""
import itertools
n, m = input("enter n,m:").split()
m1=int(m)
lst=list(n)
lst=sorted(lst,reverse=False)
per_lst=[]

def permu(lst,i):
        lst1=[]
        perm=itertools.combinations(lst,i)
        lst1.extend(perm)
        return lst1
def join_sort(lst_perm1):
    lst_join=[]
    for i2 in lst_perm1:
        str1=''.join(i2)
        lst_join.append(str1)
    sort_lst_join=sorted(lst_join,reverse=False)
    return sort_lst_join

result=[]
for i in range(1,m1+1):
    perm1=permu(lst,i)
    res1=join_sort(perm1)
    result.extend(res1)

for i3 in result:
    print(i3)
