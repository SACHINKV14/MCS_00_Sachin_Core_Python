#tik tok toe

def winner(a):
    if a=="X":
        print("player 1 won\nplayer 1's symbol is \"X\"")
    elif a=="O":
        print("player 2 won\nplayer 2's symbol is \"0\"")
val=["X","O"]
def check(val):
    for i in val:
        if (d3[1] == d3[2] == d3[3] == i) or (d3[4] == d3[5] == d3[6] == i) or (d3[7] == d3[8] == d3[9] == i):
            winner(i)
        elif (d3[1] == d3[4] == d3[7] == i) or (d3[2] == d3[5] ==  d3[8] == i) or (d3[3] == d3[6] == d3[9] == i):
            winner(i)
        elif (d3[1] == d3[5] == d3[9] == i) or (d3[7] == d3[5] == d3[9] == i):
            winner(i)

flag=True
count=0
d3={}

while(flag):
    p1=int(input("player1 enter a number(1-9):"))
    if p1 not in d3:
        d3[p1]="X"
        count += 1
        if count >= 9:
            flag = False
    else:
        continue

    if(flag):
        p2 = int(input("palyer 2 enter a number(1-9)"))
        if p2 not in d3:
            d3[p2] = "O"
            count+=1
            if count >= 9:
                flag = False
        else:
            continue

# print(d3)
d4=dict(sorted(d3.items(),key=lambda x:x[0]))
# print(d4)
list1=[x for x in d4.values()]
print(f'dict values is:{list1}')

#printing values
for i1 in [0,3,6]:
    print(list1[i1:3+i1:1])

value=d3.values()
check(val)
