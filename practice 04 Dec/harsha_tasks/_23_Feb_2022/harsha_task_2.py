lst1=[1,2,1,3,4,5,7,4,2,5,9,2,6,8,3,8]

lst2 = []
dict1 = {}
for i in lst1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

sum = 0
for i, j in dict1.items():
    sum += pow(i, j)
    print(list(str(i) * j),"----------:",pow(i, j))

print("the sum of values is", sum)