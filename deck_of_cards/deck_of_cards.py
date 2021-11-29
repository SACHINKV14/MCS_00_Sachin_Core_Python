deck_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
deck_name = [str(x) + y for x in deck_num for y in ['\u2666', '\u2665', '\u2663', '\u2660']]
val = [i for i in range(2, 15, 1) for j in range(0, 4, 1)]
deck = dict(zip(deck_name, val))
rand_num=random.random(3,15)
list1=[i for i in deck.keys()]
for i1 in range(rand_num):
    for i,j in zip(list1[1::2],list1[0: : 2]):

        d1 = {k1: v1 for k1, v1 in deck.items() if k1 in list1[1::2]}
        list11 = [i11 for i11 in d1.keys()]
        d11={k11: v11 for k11, v11 in d1.items() if k11 in list11[1::2]}
        list12 = [i12 for i12 in d1.keys()]
        d12={k12: v12 for k12, v12 in d1.items() if k12 in list12[::2]}

        d2 = {k2: v2 for k2, v2 in deck.items() if k2 in list1[::2]}
        list21 = [i21 for i21 in d2.keys()]
        d21 = {k21: v21 for k21, v21 in d2.items() if k21 in list21[1::2]}
        list22 = [i22 for i22 in d2.keys()]
        d22 = {k22: v22 for k22, v22 in d2.items() if k22 in list1[::2]}


