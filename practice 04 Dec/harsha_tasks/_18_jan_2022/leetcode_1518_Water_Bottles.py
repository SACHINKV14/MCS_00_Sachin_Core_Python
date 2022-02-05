"""
1518. Water Bottles
There are numBottles water bottles that are initially full of water.
You can exchange numExchange empty water bottles from the market with one full water bottle.
The operation of drinking a full water bottle turns it into an empty bottle.
Given the two integers numBottles and numExchange,
return the maximum number of water bottles you can drink.
Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 15 + 3 + 1 = 19.
"""

print("----------------Method 1--------------")
class Solution:
    def water_bottles(self,numBottles,numExchange):
        a = numBottles // numExchange
        if a > numExchange and a % numExchange == 0:
            print(numBottles + a)
        else:
            b = a // numExchange
            print(numBottles + a + b)

numBottles = 10001
numExchange = 2

# numBottles = 15
# numExchange = 4

# numBottles = 9
# numExchange = 3

s1=Solution()
s1.water_bottles(numBottles,numExchange)

print("----------------Method 2--------------")
def water(fill,empty):
    count=fill
    filled_list=['x' for x in range(count)]
    empty_list=[filled_list[x:x+empty] for x in range(0,len(filled_list),empty)]
    for x in empty_list:
        if len(x)== empty:
            count+=1
    print(count)
water(15,4)


