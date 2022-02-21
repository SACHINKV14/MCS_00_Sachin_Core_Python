n=int(input("enter number:"))
import math
a=1
lst=[]
while a<n+1:
    for i in range(1000):
        if i%2!=0:
            lst.append(i)
            a+=1
            if a>n:
                break
h="H"
b=' '

for i2 in lst:
    print(int((((n*2)-1)- (i2 * len(h))) / 2) * b,end="")
    print(h*i2)

for i5 in range(n+1):
    print((int(n/2)) * " ", end="")
    print(h*n,end=" ")
    print(((n*3)-1)*' ',end="")
    print(h*n)

for i4 in range(math.ceil(n/2)):
    print(((int(n/2)-1)) * " ",h*((n*5)))

for i6 in range(n+1):
    print((int(n/2))  * " ", end="")
    print(h*n,end=" ")
    print(((n*3)-1)*' ',end="")
    print(h*n)



for i3 in lst[::-1]:
    print((int(n+3*(n))) * " ", end="")
    print(int((((n*2)-1)- (i3 * len(h))) / 2) * b,end="")
    print(h*i3)
