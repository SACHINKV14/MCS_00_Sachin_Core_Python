"""This function returns a list of tuples. The th tuple contains the th element from each of the argument sequences or iterables.

If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence."""
"""
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
"""
# m,n=input().split()
# lst1=[]
# for i in range(int(n)):
#     lst1.append(list(map(float,input().split())))
# for j in range(int(m)):
#     sum=0
#     for i in lst1:
#         # print(i[j])
#         sum+=i[j]
#     print(sum/int(n))

print("---------------------------")

m,n=input().split()
lst1=[]
for i in range(int(n)):
    lst1.append(list(map(float,input().split())))

a=(zip(*lst1))
for i in a:
    print(sum(list(i))/int(n))
