n_subs=[90,90,90,92,90,40]

count = 0

if 90 in n_subs:
    # print("s its there")
    for i in n_subs:
         if i > 89 and i < 95:
            count = count + 1
            if count >2 and count<7:
                break
    print('he scored above 90 in three subjects')
