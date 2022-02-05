'''
279. Perfect Squares
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
n=36
lst=[]
a=0
while a<n:
    for i in range(1,n):
        a=i*i
        if a>n:
            break
        else:
            lst.append(a)
print("-----------------")

number=n
lst1 = []
for i2 in lst:
    if number%i2==0 and i2!=1:
        a=number//i2
        r_number = str(i2)
        for i in range(1, a + 1):
            lst1.append(r_number)
        print(f' sum of all the elements\"{lst1}\" gives sum {n}')
    elif number%i2!=0:
        break


lst1=[]
lst=sorted(lst,reverse=True)
# print(lst)
for i1 in lst:
    div = number // i1  # gives remainder
    # print(div)
    r_number = str(i1)
    for i in range(1,div+1):
        lst1.append(r_number)
    number = number - (i1 * div)
print(f' sum of all the elements\"{lst1}\" gives sum {n}')





