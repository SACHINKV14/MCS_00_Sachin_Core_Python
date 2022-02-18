"""
Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
"""
cube = lambda x:x*x*x

def fibonacci(n):
    # return a list of fibonacci numbers
    fn = 0
    fn = 0
    sn = 1
    lst = []
    if n < 0:
        return -1
    if n == 0:
        return lst
    if n == 1:
        lst.append(fn)
        return lst

    if n == 2:
        lst.append(fn)
        lst.append(sn)
        return lst
    else:
        lst = [0, 1]
        for i in range(n - 2):
            tn = sn + fn
            fn = sn
            sn = tn
            lst.append(tn)

        return lst


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))