"""
Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

"""
n=5
a=1
lst=[]
while a<n+1:
    for i in range(100):
        if i%2!=0:
            lst.append(i)
            a+=1
            if a>5:
                break
h="H"
b=' '
for i2 in lst:
    print(int((9- (i2 * len(h))) / 2) * b,end="")
    print(h*i2)

for i5 in range(n+1):
    print(2 * " ", end="")
    print(h*n,end=" ")
    print(14*' ',end="")
    print(h*n)

for i4 in range(n-2):
    print(1* " ",h*n*5)

for i6 in range(n+1):
    print(2 * " ", end="")
    print(h*n,end=" ")
    print(14*' ',end="")
    print(h*n)


for i3 in lst[::-1]:
    print(" "*19,int((9- (i3 * len(h))) / 2) * b,end="")
    print(h*i3)