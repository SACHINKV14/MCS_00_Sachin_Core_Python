

from itertools import permutations
p1='('
p2=')'
num=int(input("enter the number:"))
op=[i1 for i1 in p1 for j1 in range(0,num)]
cp=[i2 for i2 in p2 for j2 in range(0,num)]
# print(op)
# print(cp)
for i3 in op:
    for j3 in cp:
        print(i3,j3)