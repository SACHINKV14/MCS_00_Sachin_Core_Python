"""
1716. Calculate Money in Leetcode Bank
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the firstday.\
Every day from Tuesday to Sunday, he will put in $1 more
than the dabefore.On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37.
Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the
total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""
def calculate(arg):
    list1=[]
    count=0
    for x in range(1,arg):
        list2=[]
        for y in range(x,x+7):
            if count <arg:
                count+=1
                list2.append(y)
            else:
                pass
        if list2:
            list1.append(list2)
    print(list1)
    sum=0
    for x in list1:
        for y in x:
            sum+=y
    print(sum)

calculate(20)

