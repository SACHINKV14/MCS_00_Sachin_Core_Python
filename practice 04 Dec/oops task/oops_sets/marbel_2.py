import random

#getting marbel colors from user
def color_names(num_of_colors):
    color = set()
    # print(color)
    i1=0
    while i1!=num_of_colors:
        a=input("Enter marbel colors:").lower()
        if a not in color:
            color.add(a)
            i1+=1
    return color
print("---------------------colors------------------------------")

#getting fav colors from user
def fav_color_names(num_of_fav_colors):
    color1 = set()
    # print(color)
    i2=0
    while i2!=num_of_fav_colors:
        a1=input("Enter your favorite marbel colors:").lower()
        if a1 in marbels:
            color1.add(a1)
            i2+=1
    return color1

def shuffling_distributing(marbels):
    shuffled_colors = marbels.copy()
    random.shuffle(shuffled_colors)
    player1_color = [k1 for k1 in shuffled_colors[::2]]
    player2_color = [k2 for k2 in shuffled_colors[1::2]]
    p1_colors = set(player1_color)
    p2_colors = set(player2_color)
    return p1_colors,p2_colors

def score_count(player1_colors,player2_colors):
    playr1 = p1_fav_colors.intersection(player1_colors)
    playr2 = p2_fav_colors.intersection(player2_colors)
    p1_scr = len(playr1)
    p2_scr = len(playr2)
    print("-----------------------------")
    print(f'player 1 got marbel which is his favorite are:{playr1}')
    print(f'player 2 got marbel which is his favorite are:{playr2}')
    return p1_scr,p2_scr

def game_result(p1_count,p2_count):
    print("------Result-------")
    if p1_count>p2_count:
        print("\tPlayer 1 won")
    elif p1_count<p2_count:
        print("\tPlayer 2 won")
    else:
        print("Tie")
    print("------Result-------")


#main
total_colors=color_names(8)
marbels=list(total_colors)
print(total_colors)

print("-------------------------------------------------------------")

print("player1 choose your 5 favorite colors in the colors below:",'\n',total_colors)
p1_fav_colors=fav_color_names(5)
print("player2 choose your 5 favorite colors in the colors below:",'\n',total_colors)
p2_fav_colors=fav_color_names(5)

print("-------------------------------------------------------------")
print(f'palyer 1\'s favorite colors are:{p1_fav_colors}')
print(f'palyer 2\'s favorite colors are:{p2_fav_colors}')
print("-------------------------------------------------------------")

player1_colors,player2_colors=shuffling_distributing(marbels)
print(f'player 1 got:{player1_colors} ')
print(f'player 2 got:{player2_colors} ')

p1_count,p2_count=score_count(player1_colors,player2_colors)
print("-----------------------------")
print(f'player 1 score is:\"{p1_count}\" ')
print(f'player 2 score is:\"{p2_count}\" ')
print("-----------------------------")

game_result(p1_count,p2_count)



