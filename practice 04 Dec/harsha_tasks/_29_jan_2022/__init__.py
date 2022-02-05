s = "3[a]2[bc]"
s=s.replace('[','*')
s=s.replace(']','')
lst=[]
for i in s:
    if i.isnumeric():
        lst.append(i)
lst.sort(reverse=False)
print(lst)
for j in lst:
    if j in s:
        
        a=int(j)*s[s.find(j)+1::]
        print('a:',a)
        s=s.replace('s[s.find(j)+1::]','a')
        print('s:',s)
