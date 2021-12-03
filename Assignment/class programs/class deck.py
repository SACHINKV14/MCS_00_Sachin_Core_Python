import random
class Deck:
    def create_deck(self):
        deck_num=[2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        deck_name = [str(x)+y for x in deck_num for y in ['\u2666','\u2665','\u2663','\u2660']]
        val = [i for i in range(2, 15, 1) for j in range(0, 4, 1)]
        deck = dict(zip(deck_name, val))
        return deck
        # print(deck)

    def get_players_names(self,num_players):
        for i1 in range(num_players):
            b=input("Enter the Player"+str(i1+1)+"_name:").capitalize()
            a.append(b)
        return a
        print(a)

    def shuffle(self):
        s_deck = dict(sorted(deck1.items(), key=lambda x: random.random()))
        return s_deck

    def distributing_cards(self):
        player1_cards = {}
        player2_cards = {}
        list1=[i for i in dict2.keys()]

        for i,j in zip(list1[1::2],list1[0: : 2]):
            player1_cards = {k: v for k, v in dict2.items() if k in list1[1::2]}
            player2_cards = {k: v for k, v in dict2.items() if k in list1[::2]}
            print('\n remaining dictionary:',dict2)
        # print("player1 cards:",player1_cards)
        # print("player1 cards:",player2_cards)
        return player1_cards,player2_cards

    def result(self):
        print("------Result-------")
        if player1_score < player2_score:
            print('\t' + str(player2) + ' ' + 'Won')
        elif player1_score > player2_score:
            print('\t' + str(player1) + ' ' + 'Won')
        else:
            print("Tie")
        print("------Result-------")




num_players=2
a=[]
play=Deck()
deck1=play.create_deck()
print("deck1:",deck1)
player1,player2=play.get_players_names(num_players)
print("player1 is:",player1)
print("player2 is:",player2)
shuffle_deck=play.shuffle()
print(shuffle_deck)

dict2=shuffle_deck

player1_card,player2_card=play.distributing_cards()


print(str(player1)+ '\t'+'cards:',player1_card)
print(str(player2)+ '\t'+'cards:',player2_card)
#
player1_score=sum(player1_card.values())
print(str(player1)+ '\t'+'score:',player1_score)
player2_score=sum(player2_card.values())
print(str(player2)+ '\t'+'score:',player2_score)
play.result()
