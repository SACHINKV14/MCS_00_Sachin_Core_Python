str1='zero one two three four five six seven eight nine'
str2='fviefuro'
s_lst1=list(str2)
s_lst2=s_lst1.copy
list1=list(str1.split())
lst2=[]
for i in list1:
    lst2.append(list(i))
# print('lst2',lst2)
lst3=[]
for num in lst2:
    s_lst2 = s_lst1.copy()
    for i in s_lst2:
        if i in num:
            num.remove(i)
    print('num',num)
    lst3.append(num)
    print('----------')


print("--------creating number and finding values---------------")
num=[]
i=0
for x in lst3 :
    if x == []:
        num.append(str(i))
    i = i + 1
num1=''.join(num)
print(num1)
