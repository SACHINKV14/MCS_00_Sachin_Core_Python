"""The defaultdict tool is a container in the collections class of Python.
It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value if that key has not been set yet.' \
 If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
"""

A,B=map(int,input().split())
lstA=[]
lstB=[]
for i1 in range(A):
    n1=input()
    lstA.append(n1)

for i2 in range(B):
    n2=input()
    lstB.append(n2)

for k in range(B):
    for i,j in enumerate(lstA):
        if lstB[k] not in lstA:
            print(-1)
            break

        else:
            if j == lstB[k]:
                print(i + 1, end=" ")
    print()
