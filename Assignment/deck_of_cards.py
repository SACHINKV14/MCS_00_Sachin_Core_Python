deck = [str(x)+y for x in range(1,14) for y in ["S","H","C","D"]]
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



import random

keys = list(deck_cards.keys())
random.shuffle(keys)

Shuffled_deck_cards = dict()
for key in keys:
    Shuffled_deck_cards.update({key: deck_cards[key]})
print("Dictionary after Shuffling :\n ",Shuffled_deck_cards)


player1 = "tom"
player2 = "Jerry"
print("player1 name is:",player1)
print("player2 name is:",player2)
key_list=[]
player1_cards ={}
player2_cards={}

for i12 in Shuffled_deck_cards.keys():
    key_list.append(i12)

player1_cards = {k: v for k, v in Shuffled_deck_cards.items() if k in key_list[1::2]}
player2_cards = {k: v for k, v in Shuffled_deck_cards.items() if k in key_list[::2]}
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
