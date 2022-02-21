m,n=input().split(" ")
N=7;M=21
a=".|."
b='-'
c="WELCOME"
lst=[x for x in range(1,N,2)]
rev_lst=lst[::-1]

for i in lst:
    print(int((M-(i*len(a)))/2)*b,end="")
    print(a*i,end="")
    print(int((M-(i*len(a)))/2)* b)

print(int((M-(len(c)))/2)*b,end="")
print(c,end="")
print(int((M-(len(c)))/2)*b)


for i in rev_lst:
    print(int((M-(i*len(a)))/2)*b,end="")
    print(a*i,end="")
    print(int((M-(i*len(a)))/2)* b)


