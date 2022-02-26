"""
Concept
If the inputs are given on one line separated by a character (the delimiter), 
use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) 
by default. To specify that comma is the delimiter, use string.split(','). For this challenge, 
and in general on HackerRank, space will be the delimiter.
"""
num1=int(input())
set1=set(map(int,input().split()))
num2=int(input())
set2=set(map(int,input().split()))


set1.symmetric_difference_update(set2)

set3=sorted(set1,reverse=False)
for i in set3:
    print(i)


