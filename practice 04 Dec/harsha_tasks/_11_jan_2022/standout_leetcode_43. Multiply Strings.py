"""
43. Multiply Strings
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

"""
# #example 1
# num1 = "2"
# num2 = "3"
#example 2
num1 = "123"
num2 = "456"
n1=int(num1)
n2=int(num2)
n3=n1*n2
res=str(n3)
print('result is:',res)