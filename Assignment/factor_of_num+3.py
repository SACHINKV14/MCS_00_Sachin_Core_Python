# a=[1,2,3,5,4,6,7,8,9,1,3,5,6,8]
# b=set(a)
# print(b)
# c=()
# l=int(len(b)/2)
# for i in range(1,l):
#     for j in range(l,len(b)+1):
#         if i+j==7:
#             c=i,j
#             print(c)
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
flag2 = 0
a1=a
b=set(a1)
c=()
l=int(len(b)/2)
for i in range(1,l):
    for j in range(l,len(b)+1):
        if i+j==7:
            c=i,j
            print(c)