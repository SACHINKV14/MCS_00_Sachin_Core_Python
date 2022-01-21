def superdigit(num):
    st=str(num)
    sum =0
    for i in st:
        sum +=int(i)
    if sum>9:
        return superdigit(sum)
    else:
        return sum

#9875987598759875
a=superdigit(9875)
print(a)