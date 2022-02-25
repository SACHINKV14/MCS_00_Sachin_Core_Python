lst=[9,5,8]
sum1=0
lst2=[]
total=lst[0]
for i,j in enumerate(lst):
    sum1+=(i+1)*j
    total+=sum1
    lst2.append(sum1)
print(lst2)
print(sum(lst2))