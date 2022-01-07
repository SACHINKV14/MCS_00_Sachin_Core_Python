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

shuffled_colors=marbels.copy()
# print(shuffled_colors)
import random
random.shuffle(shuffled_colors)
# print(shuffled_colors)
print("-------------------------------------------------------------")
player1_color = [k1 for k1 in shuffled_colors if k1 in shuffled_colors[::2]]
player2_color = [k2 for k2 in shuffled_colors if k2 in shuffled_colors[1::2]]
player1_colors=set(player1_color)
print(f'player 1 got:{player1_colors} ')
player2_colors=set(player2_color)
print(f'player 2 got:{player2_colors} ')

playr1 = p1_fav_colors.intersection(player1_colors)
playr2 = p2_fav_colors.intersection(player2_colors)


p1_count=len(playr1)
p2_count=len(playr2)
print("-----------------------------")
print(f'player 1 got marbel which is his favorite are:{playr1}')
print(f'player 2 got marbel which is his favorite are:{playr2}')
print("-----------------------------")
print(f'player 1 score is:\"{p1_count}\" ')
print(f'player 2 score is:\"{p2_count}\" ')
print("-----------------------------")

print("------Result-------")
if p1_count>p2_count:
    print("Player 1 won")
elif p1_count<p2_count:
    print("Player 2 won")
else:
    print("Tie")
print("------Result-------")

#
