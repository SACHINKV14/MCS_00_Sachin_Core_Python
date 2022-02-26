"""input()
In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).
"""
m,n=input().split()
m=int(m)
n=int(n)

sum=0
for i in range(n):
    a=pow(m,i)
    sum+=a

if sum==n:
    print(True)
else:
    print(False)

print("-----------------------")
m,n=input().split()
m=int(m)
x=int(n)
expr=int(n)
y = eval(expr)

if sum==y:
    print(True)
else:
    print(False)