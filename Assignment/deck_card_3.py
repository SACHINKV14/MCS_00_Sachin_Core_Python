# imports random
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1, 14), ['Spade', 'Heart',
'Diamond', 'Club']))
print(type(deck))
# shuffles the deck
random.shuffle(deck)

# draw five cards
howmany = int(input('How many cards do you want to display? '))
print('You got:')
for i in range(howmany):
    print(deck[i][0], 'of', deck[i][1])

    # import random
    # a=random.randint(1,15)
    # b=random.randint(1,15)
    # print(a)
    #
    # player1_cards={}
    # player2_cards={}
    # for i in range(0,53,a):
    #     for j in range(0,53,a):

