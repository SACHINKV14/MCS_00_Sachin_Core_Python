
class Game:
    def table_guess(self,num_q,table):
        score=[]
        for i in range(num_q):
            num1 = random.randint(2, table)
            num2 = random.randint(2, table)
            print(f'{num1} * {num2}')
            ans=int(input("answer="))
            if ans==num1*num2:
                score.append(1)
            else:
                score.append(0)
        return score
import random
# table=int(input("enter table which you know:"))
num_q=3
table=9
t1=Game()
print("player1")
player1=t1.table_guess(num_q,table)
print("--------------------------------")
print("player2")
player2=t1.table_guess(num_q,table)
print("--------------------------------")
attempt=[]
for i in range(1,num_q+1):
    attempt.append('attempt'+str(i))

print("attempts  p1_score  p2_score")
for i in range(len(player1)):
    print(f'{attempt[i]}\t\t{player1[i]}\t\t{player2[i]}')
print("-------------------")
p1_count=sum(player1)
p2_count=sum(player2)
print(f'player1 score={p1_count}\nplayer2 score={p2_count}')
print("------Result-------")
if p1_count > p2_count:
    print("\tPlayer 1 won")
elif p1_count < p2_count:
    print("\tPlayer 2 won")
else:
    print("\t\tTie")
print("------Result-------")