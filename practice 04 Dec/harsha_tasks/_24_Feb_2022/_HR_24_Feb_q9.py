# s = input()
s="qwertyuiopasdfghjklzxcvbnm"
lst1=[]
for i in s:
    if i not in lst1:
        lst1.append(i)
dict2={}
for i2 in lst1:
    dict2[i2]=s.count(i2)
dict3=dict(sorted(dict2.items(),key=lambda x:x[1],reverse=True))
count1=0
for i,j in dict3.items():
    print(i,j)
    count1 += 1
    if count1 >= 3:
        break
    else:
        continue
