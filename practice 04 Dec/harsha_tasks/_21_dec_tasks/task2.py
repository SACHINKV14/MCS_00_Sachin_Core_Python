from itertools import permutations
str1='()'
num=int(input("enter the number:"))

val=[i for i in str1 for j in range(0,num)]
print(val)
perm = permutations(val, len(val))
result=list(perm)
# print(result)
print(len(result))
str2=""
lst1=[]
for i1 in result:
    i1=list(i1)
    # i1+=str2
    print(i1)
