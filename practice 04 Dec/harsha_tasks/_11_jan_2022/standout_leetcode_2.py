# 2. Add Two Numbers
'''
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''
#example 1
# l1 = [2,4,3]
# l2 = [5,6,4]
#example 2
# l1 = [0]
# l2 = [0]
#example 3
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]


l1_r=l1[::-1]
l2_r=l2[::-1]
str1="".join(map(str,l1_r))
str2="".join(map(str,l2_r))
num1=int(str1)
num2=int(str2)
num3=str(num1+num2)
# print(num3)
n=num3[::-1]
res=[int(i) for i in n]
print('result is:',res)

