import itertools

x=2;y=2;z=2;n=2
lst=[2,2,2]


res=[]
for i1 in range(x+1):
    for j1 in range(y+1):
        for k1 in range(z+1):
            a=[i1,j1,k1]
            if sum(a) != n:
                res.append(a)

print(res)