"""67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
# a = "11"
# b = "1"

a = "1010"
b = "1011"

res = int(a,2)+int(b,2)     #(remember, the base for binary values is 2).
res_bin =bin(res)           #convert int to binary
z=str(res_bin)
z=z.replace("0b","")        #to remove 0b
print(z)