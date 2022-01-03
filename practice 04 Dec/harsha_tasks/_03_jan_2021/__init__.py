def d_fact(x):
    if x==1:
        return x
    else:
        return(x*d_fact(x-1))

x=5
r=2
a=d_fact(x)
print(a)
b=d_fact(x-r)
print(b)