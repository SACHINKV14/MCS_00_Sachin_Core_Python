from random import randint
dict1={'p1':0,'p2':0,'p3':4,'p4':0,'p5':0}
#
# clap=['h','t']
# for k,v in dict1.items():
#     b=randint(0,1)
#     dict1[k]=clap[b]
#
# print(dict1)

lst=[0,0,0,0,0]
while True:
    clap=['h','t']
    for i in range(len(lst)):
        b=randint(0,1)
        lst[i]=clap[b]
    print(lst)

    print('h count',lst.count('h'))
    print('t count',lst.count('t'))
    h=lst.count('h')
    t=lst.count('t')
    if h==1:
        print('h count')
        lst.remove('h')
        print(lst)
    elif t==1:
        print('t count')
        lst.remove('t')
        print(lst)
    else:
        pass

    if len(lst)!=1:
        continue
    else:
        break

print('final',lst)