import random
print("-------------create deck names-------------")
deck_num=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
deck_name = [str(x)+y for x in deck_num for y in ['\u2666','\u2665','\u2663','\u2660']]
print(deck_name)
print("-------------------------------------------")
'''        to genarate values 
# for i in range(2,15,1):
#     for j in range(0,4,1):
#         val.append(i)
# print(val)
# 
# or 
#
# val=[i for i in range(2,15,1) for j in range(0,4,1)]
'''
print("----------Assign values for deck-------------")
val=[i for i in range(2,15,1) for j in range(0,4,1)]
print(val)
print("---------------------------------------------")

print("-----------create dictionary----------")
deck=dict(zip(deck_name, val))
print(deck)
print("--------------------------------------")

# print("----------functioin to get players name------------")
def get_players_names(num_players):
    for i1 in range(num_players):
        b=input("Enter the Player"+str(i1+1)+"_name:").capitalize()
        a.append(b)
    return a

# print("--------------------------------------")



print("----------------welcome!----------------")
print("---------To Play Deck of Cards-------------- ")

num_players=2
a=[]
player1,player2=get_players_names(num_players)
print("player1 is:",player1)
print("player2 is:",player2)

# print("--------------------------shuffling done here----------------")
# using same deck name for if i remove shuffle need to distribute crads without shuffling
deck = dict(sorted(deck.items(), key=lambda x: random.random()))
# print(type(deck))
# print(deck)
#print("-----------shuffling has done----------------")

dict1=deck
print(type(dict1))
player1_cards={}
player2_cards={}
list1=[i for i in dict1.keys()]

for i,j in zip(list1[1::2],list1[0: : 2]):
    player1_cards = {k: v for k, v in dict1.items() if k in list1[1::2]}
    player2_cards = {k: v for k, v in dict1.items() if k in list1[::2]}
    # print('\n remaining dictionary:',dict1)

print(str(player1)+ '\t'+'cards:',player1_cards)
print(str(player2)+ '\t'+'cards:',player2_cards)

player1_score=sum(player1_cards.values())
print(str(player1)+ '\t'+'score:',player1_score)
player2_score=sum(player2_cards.values())
print(str(player2)+ '\t'+'score:',player2_score)

print("------Result-------")
if player1_score<player2_score:
    print('\t'+str(player2)+'\t' +'Won')
elif player1_score>player2_score:
    print('\t'+str(player1)+'\t' +'Won')
else:
    print("Tie")
print("------Result-------")











