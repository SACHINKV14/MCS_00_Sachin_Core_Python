lst1=[[1,2,3,4,5,6,7],(1,2),(),(3,4,5,6)]
print(lst1)
for ele in lst1:
    print(len(ele))
    if len(ele) ==0:
        lst1.remove(ele)

print(lst1)