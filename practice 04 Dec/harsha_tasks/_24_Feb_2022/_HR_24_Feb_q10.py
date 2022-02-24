arr=[[11,2,4],[4,5,6],[10,8,-12]]
arr2=[]
for i1 in arr:
    arr2.append(i1[::-1])


sum1=0
sum2=0
for i in range(len(arr)):
    sum1+=arr[i][i]
    sum2+=arr2[i][i]
print(abs(sum1-sum2))


