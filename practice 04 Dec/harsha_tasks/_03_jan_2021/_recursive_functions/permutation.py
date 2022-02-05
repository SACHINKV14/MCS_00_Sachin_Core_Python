#nPk = n!/(n − k)!
#n*n-1*n-2...1   5
#k=2  5-2=3! 3*2*1
def fact(x):
    if x == 0 or x==1:
        return 1
    else:
        return (x * fact(x-1))   #1,2,3,4,5

num = 5
#numerator factorial
numera=fact(num)
r=2
# print(numera)
denami=fact(num-r)
# print(denami)
permu=numera/denami
print(f'permatation of {num}p{r} is: {permu}')