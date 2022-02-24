str1="0000000092000.000000166.0000000/24"
a=str1.split(".")
lst=[]
for i in a:
    a1=i.lstrip("0")
    if a1[0]!="/":
        lst.append(a1)
    elif a1[0]=="/":
        print("mask is:",a1[1::])

str2=".".join(lst)
print("ip is",str2)

