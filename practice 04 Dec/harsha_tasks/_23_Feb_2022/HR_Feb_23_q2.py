"""
You are given  words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.
Note: Each input line ends with a "\n" character.
"""

n=int(input())
lst=[]
for i in range(n):
    lst.append(input())

lst1=[]
for j in lst:
    if j not in lst1:
        lst1.append(j)
print(len(lst1))
for k in lst1:
    print(lst.count(k),end=" ")

print("--------------------------")
n=int(input())
lst1=[]
for i in range(n):
    str1=input()
    lst1.append(str1)
dict={}
for j in lst1:
    if j not in dict:
        dict[j]=1
    else:
        dict[j]+=1

print(len(dict))
for i,j in dict.items():
    print(j,end=" ")




