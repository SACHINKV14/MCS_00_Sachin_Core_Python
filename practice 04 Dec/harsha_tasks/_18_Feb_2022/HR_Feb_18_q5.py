# Collections.namedtuple() in Python - Hacker Rank Solution
# Python 3
# Enter your code here. Read input from STDIN. Print output to STDOUT
# Collections.namedtuple() in Python - Hacker Rank Solution START
import collections

n = int(input())
scol = ','.join(input().split())
Student = collections.namedtuple('Student',scol)

sum = 0
for i in range(n):
    row = input().split()
    student = Student(*row)
    sum += int(student.MARKS)

print(sum/n)
# Collections.namedtuple() in Python - Hacker Rank Solution END