import random
# print("-------------create deck names-------------")
deck_num=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
deck_name = [str(x)+y for x in deck_num for y in ['\u2666','\u2665','\u2663','\u2660']]
# print(deck_name)
val=[i for i in range(2,15,1) for j in range(0,4,1)]

deck=dict(zip(deck_name, val))
# print(deck)

a=random.randint(3,15)
print(a)

list1=deck.keys