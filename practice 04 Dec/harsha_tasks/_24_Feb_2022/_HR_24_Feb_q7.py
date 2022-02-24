"""
You are given string  and number .

Consider a substring  of string .
For each position of string  mark it if there is an occurence of the substring that
covers the position. More formally, position  will be marked if there exists such index  that:
and . We will tell  produce  islands if all the marked positions form  groups of
contiguous positions.

For example, if we have a string ababaewabaq the substring aba marks the
positions 1, 2, 3, 4, 5, 8, 9, 10; that is XXXXXewXXXq (X denotes marked position). We can see 2 groups of contiguous positions, that is 2 islands. Finally, substring aba produces 2 islands in the string ababaewabaq.

Calculate and print the number of different substrings of string  that produce exactly  islands.
"""
from itertools import combinations

def letterIslands(s, k):
    # Write your code here
    for i in range(k):
        print(i)
        perm=combinations(s,i+1)
        for k1 in perm:
            print(k1)
    return "done"

if __name__ == '__main__':
    s = input()

    k = int(input().strip())

    result = letterIslands(s, k)
    print(result)
