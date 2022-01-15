"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
"""
"""Approach: The idea is to use the ASCII value of the digits from 0 to 9 start from 48 – 57.
Therefore, to change the numeric character to an integer subtract 48 from 
the ASCII value of the character will give the corresponding digit for the given character."""
# Function to convert string to
# integer without using functions
def convert(s):
    # Initialize a variable
    num = 0
    n = len(s)

    # Iterate till length of the string
    for i in s:
        # Subtract 48 from the current digit
        num = num * 10 + (ord(i) - 48)

        # Print the answer
    return num

# Given string of number
# num1 = "2"
# num2 = "3"

num1 = "123"
num2 = "456"

# Function Call
n1=convert(num1)
n2=convert(num2)
result=str(n1*n2)
print(result)

