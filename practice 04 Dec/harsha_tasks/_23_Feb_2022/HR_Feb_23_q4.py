"""collections.deque()
A deque is a double-ended queue. It can be used to add or remove elements from both ends.

Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

Click on the link to learn more about deque() methods.
Click on the link to learn more about various approaches to working with deques:"""




n=int(input())
lst1=[]
for i in range(n):
    lst1.append(input())


lstres=[]
for i in lst1:
    ins=[val1 for val1 in i.split() if val1.isalpha()]
    val=[int(val2) for val2 in i.split() if val2.isdigit()]
    if ins[0]=="append":
        lstres.append(val)
    if ins[0]=="appendleft":
        lstres.insert(0,val)
    if ins[0]=="clear":
        lstres.clear()
    if ins[0]=="extend":
        lstres.extend(val)
    if ins[0]=="extendleft":
        lstres.extend(val)
    if ins[0]=="count":
        print(lstres.count(val))
    if ins[0]=="pop":
        lstres.pop()
    if ins[0]=="popleft":
        lstres.pop(0)
    if ins[0]=="remove":
        lstres.remove(val)
    if ins[0]=="reverse":
        lstres = lstres.reverse()
    if ins[0]=="rotate":
        lstres[val:]=lstres[:val]

for i in lstres:
    for j in i:
        print(j,end=" ")