"""
264. Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

"""

"""not completed"""
n=10
lst1=[2,3,5]
lst2=[]


for i in range(1,n+n):
    if len(lst2)>=n:
        break
    else:
        for j in range(2,i):
            if i%j==0 and j not in lst1:
                break

        else:
            lst2.append((i))

print(lst2)