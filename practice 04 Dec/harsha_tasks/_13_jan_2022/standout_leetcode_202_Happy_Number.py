

num=int(input("enter the number"))

while num>10:
    res=0
    num1=str(num)
    for i in num1:
        res=res+int(i)*int(i)

    print(num1[0],"^2",'+',num1[1],"^2",'=',res)
    num=res
if num!=1:
    print("unhappy number")
else:
    print("happy number")


