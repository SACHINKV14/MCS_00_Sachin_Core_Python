"""Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
Using the information given below,
determine the number of apples and oranges that land on Sam's house.
In the diagram below:
The red region denotes the house, where  is the start point, and  is the endpoint.
The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point ,
and the orange tree is at point .
When a fruit falls from its tree,
it lands  units of distance from its tree of origin along the -axis.
*A negative value of  means the fruit fell  units to the tree's left,
and a positive value of  means it falls  units to the tree's right. *"""

def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apple=0
    for i in apples:
        ap_a=a+i
        if ap_a>=s and ap_a<=t:
            count_apple+=1
    count_orange=0
    for i2 in oranges:
        op_b=b+i2
        if op_b>=s and op_b<=t:
            count_orange+=1

    print(count_apple)
    print(count_orange)



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
