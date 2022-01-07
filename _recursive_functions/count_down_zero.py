def countdown(num):
    print(num)
    if num==0:
        return
    else:
        countdown(num-1)

countdown(5)
