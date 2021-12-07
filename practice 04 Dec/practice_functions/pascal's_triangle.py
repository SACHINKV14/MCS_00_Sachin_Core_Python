'''Pascal’s triangle is a pattern of the triangle which is based on nCr,
below is the pictorial representation of Pascal’s triangle.
Input: N = 5
Output:
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
  Time Complexity: O(N)

However, this approach is applicable up to n=5 only.
'''

# Print Pascal's Triangle in Python
from math import factorial

# input n
n = 5
for i in range(n):
    for j in range(n - i + 1):
        # for left spacing
        print(end=" ")

    for j in range(i + 1):
        # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")

    # for new line
    print()

print("-----------------------------")
'''Method 2: We can optimize the above code by the following concept of a Binomial Coefficient,
 the i’th entry in a line number line is Binomial Coefficient C(line, i) and all lines start with value 1.
 The idea is to calculate C(line, i) using C(line, i-1).
 C(line, i) = C(line, i-1) * (line - i + 1) / i
 '''

# Print Pascal's Triangle in Python

# input n
n = 5

for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(' ', end='')

    # first element is always 1
    C = 1
    for j in range(1, i + 1):
        # first value in a line is always 1
        print(' ', C, sep='', end='')

        # using Binomial Coefficient
        C = C * (i - j) // j
    print()

print("---------------------------")
'''Method 3: This is the most optimized approach to print Pascal’s triangle, 
this approach is based on powers of 11.
11**0 = 1
11**1 = 11
11**2 = 121
11**3 = 1331
'''

# Print Pascal's Triangle in Python

# input n
n = 5

# iterarte upto n
for i in range(n):
    # adjust space
    print(' ' * (n - i), end='')

    # compute power of 11
    print(' '.join(map(str, str(11 ** i))))