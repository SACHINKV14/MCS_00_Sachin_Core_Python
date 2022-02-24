"""You are choreographing a circus show with various animals.
For one act, you are given two kangaroos on a number line ready
to jump in the positive direction (i.e, toward positive infinity).
The first kangaroo starts at location  and moves at a rate of  meters per jump.
The second kangaroo starts at location  and moves at a rate of  meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible,
return YES, otherwise return NO.
"""
def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        if x1+v1==x2+v2:
            a="YES"
            break
        x1 = x1 + v1
        x2 = x2 + v2
    else:
        a="NO"
    return a

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)
    print(result)


