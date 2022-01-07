#nPk = n!/(n − k)!

def fact(x):
    if x == 0 or x==1:
        return 1
    else:
        return (x * fact(x-1))

num = 5
#numerator factorial
numera=fact(num)
r=2
# print(numera)
denami=fact(num-r)
# print(denami)
permu=numera/denami
print(f'permatation of {num}p{r} is: {permu}')