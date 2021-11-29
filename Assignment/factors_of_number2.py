
D=[]
z=1

flag1=1
while flag1:
    a=input("Enter the number:")
    if a.isalpha():
        print("enter only number")
        flag = -1
    elif a.isnumeric():
        D.append(a)
        flag2 = 1
        # print("---------should go here-----------")
        y = input("Want to add another number?press (y/n):")
        # print(y)
        # print(type(y))
        if y == 'y':
            flag = 1
        elif y == 'n':
            flag = 0
        else:
            flag = -1
            print("WRONG INPUT.Enter : ")

    else:
        print("enter only number")

print("you have entered:",D)
b=set(D)          #to remove duplicate
# print(b)
a=list(b)
c=()
l=[]
# print(a)
for i in a:
    for j in a:
        if(i+j==7):
                c=i,j
                a.remove(j)
                l.append(c)
                # print(c)
print(l)