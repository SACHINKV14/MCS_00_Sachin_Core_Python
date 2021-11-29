a=[]
flag2 = 1
while(flag2):
    if(flag2 != -1):
        user_input = int(input("Enter single digit numbers : "))
        a.append(user_input)
    another_input = input("Do you want to enter another input (y/n) : ")
    if (another_input == "y"):
        flag2 = 1
    elif (another_input == "n"):
        flag2 = 0
    else:
        print("WRONG INPUT. ENTER input AGAIN : ")
        flag2 = -1
print(a)
b=set(a)          #to remove duplicate
print(b)
c=()
for i in b:
    for j in b:
        if(i+j==7):
            c=i,j
        print(type(c))
