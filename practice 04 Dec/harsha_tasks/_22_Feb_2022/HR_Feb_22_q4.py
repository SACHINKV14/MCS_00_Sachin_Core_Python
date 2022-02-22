"""
You are given a positive integer .
Print a numerical triangle of height  like the one below:

"""

for i in range(1,int(input())):
    print(int(i * 10**i / 9))

