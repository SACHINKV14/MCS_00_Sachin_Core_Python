"""204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""
lst=[]
num=int(input("enter th number range:"))
for i in range(2,num+1):
    for j in range(2,i-1):
        if i%j == 0:
            break
    else:
        lst.append(i)
print(f'There are {len(lst)} prime numbers less than {num}, they are \n{lst}')