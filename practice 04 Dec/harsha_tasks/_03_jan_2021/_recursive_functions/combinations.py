#n!/ r!(n-r)!

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
rfact=fact(r)
permu=numera/(denami*rfact)
print(f'permatation of {num}c{r} is: {permu}')