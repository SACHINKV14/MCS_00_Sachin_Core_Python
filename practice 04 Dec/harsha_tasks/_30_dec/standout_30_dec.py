'''386. Lexicographical Numbers
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
'''
num=int(input("enter max number:"))
list1=[x for x in range(1,num)]
lst2=[]
for i in list1:
    b=str(i)
    lst2.append(b)
lst2=sorted(lst2)

lst3=[]
for j in lst2:
    c=int(j)
    lst3.append(c)
print(f'Lexicographical Numbers:\n{lst3}')