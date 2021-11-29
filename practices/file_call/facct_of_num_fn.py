from fact_of_num import y


D=[]

flag1=True
print("Enter exit to exit.")
while flag1:
    try:
        a=input("Enter the number:")
        if(a == "exit"):
            break
        D.append(int(a))
    except:
        print("Enter numbers only")

print("you have entered:",D)
b=set(D)          #to remove duplicate
# print(b)
a=list(b)
# print(a)
c=()
d=[]
y1=y
for i in a:
    for j in a:
        if(i+j==y1):
                c=i,j
                a.remove(j)
                d.append(c)
                # print(c)
print(d)