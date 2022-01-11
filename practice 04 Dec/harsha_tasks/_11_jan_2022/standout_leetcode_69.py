"""
69. Sqrt(x)
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842...,
and since the decimal part is truncated, 2 is returned.

"""

# Python Program to calculate the square root

# Note: change this value for a different result
# num = 8
num = 4

# To take the input from the user
#num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
import math
print(math.floor(num_sqrt)) # floor
print(math.trunc(num_sqrt)) # work as floor
