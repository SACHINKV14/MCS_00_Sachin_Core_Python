d={'red':1,'blue':2,'green':3,'yellow':4,'grey':5,'black':6,'white':7,'violet':8,'purple':9,'pink':10}
print(d)
p1={}
p2={}
import random
a1=random.randint(1,9)
list1=[i for i in d.keys()]
for i in list1[1::a1]:
    for j in list1[1::a1]:
        p1[i] = d[i]
        d.pop(i)
        p2[j] = d[j]
        d.pop(j)
print(p1)
print(p2)




#     p1[i]=a[i]
#     a.pop(i)
#     p2[j] = a[j]
#     a.pop(j)
# print(p1)
# print(p2)




# list1=[i for i in a.keys()]
# for i in range(1,(len(list1)+1),2):
#     for j in range(0,(len(list1)+1),2):
#         p1[i]=a[i]
#         print(p1)

#
#
# for i in range(1,len(list1)+1,2):
#     for j in range(0, len(list2) + 1, 2):
#         # p1[i]=next(iter(a))
#         p1[i]=next(iter(a.items()))[0]
# print(p1)
