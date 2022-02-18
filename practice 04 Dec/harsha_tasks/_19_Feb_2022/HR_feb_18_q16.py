def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':

    # s = "chris alan"
    # s="123sac kv"
    s="1 w 2 r 3g"
    solve(s)

