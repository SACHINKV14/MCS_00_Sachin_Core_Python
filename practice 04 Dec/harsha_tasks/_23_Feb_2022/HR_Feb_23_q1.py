"""
collections.OrderedDict
An OrderedDict is a dictionary that remembers the order of the keys that were inserted first.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.

"""
"""
lstA=[];lstB=[]
lstA.append("BANANA FRIES");lstB.append(12)
lstA.append("POTATO CHIPS");lstB.append(30)
lstA.append("APPLE JUICE");lstB.append(10)
lstA.append("CANDY");lstB.append(5)
lstA.append("APPLE JUICE");lstB.append(10)
lstA.append("CANDY");lstB.append(5)
lstA.append("CANDY");lstB.append(5)
lstA.append("CANDY");lstB.append(5)
lstA.append("POTATO CHIPS");lstB.append(30)
"""
n=int(input())
lstA=[]
lstB=[]
for i1 in range(n):
    inp = input()
    inp1 = inp.split(" ")
    B = int(inp1[-1])
    A = inp.replace(inp1[-1],"")
    A=A.rstrip()
    lstA.append(A)
    lstB.append(B)


lst3=[]
for i,j in zip(lstA,lstB):
    if i not in lst3:
        lst3.append(i)

res=[]

for i1 in lst3:
    count=0
    for i2,j2, in zip(lstA,lstB):
        if i1==i2:
            count+=j2
    res.append(count)

for i4,j4 in zip(lst3,res):
    print(i4,j4)


print("-------------------------------")
import re
n= int(input())
lst1=[]
for i in range(n):
    lst1.append(input())
dict1={}
for j in lst1:
    name1=[str(val1) for val1 in j.split() if val1.isalpha()==True]
    name=""
    for k in name1:
        name=name+" "+k
    val=[int(val2) for val2 in j.split() if val2.isdigit()==True]
    if name not in dict1:
        dict1[name]=val
    else:
        dict1[name]+=val

for i,j in dict1.items():

    print(i.lstrip(),sum(j))