def counter(num):
    if num<=0:
        return num
    else:
        return num+counter(num-1)

num=int(input("enter the nuber:"))
ans=counter(num)
print(f'sum of all numbers 0 till {num} is :{ans} ')