lst1=[1,2,3,'a',True,1.2,[1,2],{2:3},(1,2),5,6,'b']
count_num=0
for i in lst1:
    if type(i)==tuple:
        break
    else:
        count_num += 1
print(f'number of items in list before tuple is:{count_num}')
