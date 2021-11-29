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

'''print("---------------method1 start--------------")
print("-------------with loops-------------")
print("you have entered:",D)
b=set(D)          #to remove duplicate
# print(b)
a=list(b)
# print(a)
c=()
d=[]
for i in a:                 #
    for j in a:             #
        if(i+j==7):
            c=i,j
            a.remove(j)
            d.append(c)
            # print(c)
print(d)
print("---------------method1 ends--------------")
print("-------------with loops-------------")'''

'''
print("----------------------method 2 using functions and loops start-------------------------")

def get_combination(number):
    for i in l1:             #to see the number of l1 and get numbers in i
        for j in l1:         #to see the number of l1 and get numbers in j
            if(i+j==number):
                c=i,j
                l1.remove(j)
                list1.append(c)    #to make sure duplicate combition should not get
                print(c)

    return list1


n=int(input("enter the number for which u want combitionation :"))
b=set(D)
l1=list(b)
c=()
list1=[]
comb=get_combination(n)
print(comb)

print("----------------------method 2 using functions and loops ends-------------------------")
'''

print("----------------------method 3 using functions list comprehention start-------------------------")

def get_combination(number):
    l1=[c=i,j for i,j in zip(l1[0::1],l2[0::1]) if i+j==number]:       #is this possible
        if i+j==number:
            c=i,j
            l1.remove(j)
            list1.append(c)    #to make sure duplicate combition should not get
            print(c)

    return list1


n=int(input("enter the number for which u want combitionation :"))
b=set(D)
l1=list(b)
l2=l1
c=()
list1=[]
comb=get_combination(n)
print(comb)

