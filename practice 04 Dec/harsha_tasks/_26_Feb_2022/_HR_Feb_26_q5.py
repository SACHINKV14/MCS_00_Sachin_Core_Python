n = int(input())
s = set(map(int, input().split()))
num1=int(input())
str1=[]
for _ in range(num1):
    str1.append(input())

for i in str1:
    op=[str(val1) for val1 in i.split() if val1.isalpha()==True]
    val=[int(val1) for val1 in i.split() if val1.isdigit()==True]

    if op[0]=="pop":
        s.pop()
    if op[0]=="remove":
        s.remove(val[0])
    if op[0]=="discard":
        s.discard(val[0])
sum=0
for i2 in s:
    sum+=i2
print(sum)

