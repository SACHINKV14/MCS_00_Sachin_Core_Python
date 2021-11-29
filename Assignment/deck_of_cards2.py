import sys

var=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
deck = [str(x)+y for x in var for y in ["S","H","C","D"]]
val=[]
for i in range(3,16):
    for j in range(0,4):
       val.append(i)
print(val)

deck_cards = {}
# COnvert to dictionary
for key in deck:
   for value in val:
      deck_cards[key] = value
      val.remove(value)
      break
print("Dictionary Before Shuffling :\n ",deck_cards)
dict1=deck_cards
player1_cards={}
player2_cards={}

list1=[i for i in set(dict1.keys())]

for i,j in zip(list1[1::2],list1[0: : 2]):
    # print(f'\n distributing between two players')
    player1_cards[i]=dict1[i]
    dict1.pop(i)
    player2_cards[j]=dict1[j]
    dict1.pop(j)
    # print('\n remaining dictionary:',dict1)

print('tom cards:',player1_cards)
print('jerry cards:',player2_cards)

tom_score=sum(player1_cards.values())
print("tom's score is:",tom_score)
jerry_score=sum(player2_cards.values())
print("jerry's score is:",jerry_score)

print("------Result-------")
if tom_score<jerry_score:
    print("\t Jerry Won")
elif tom_score>jerry_score:
    print("\t Tom Won")
else:
    ("Tie")
print("------Result-------")
