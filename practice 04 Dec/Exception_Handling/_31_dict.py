

# num=int(input('enter number of values for dict:'))

lst1=['a','b',1]
lst2=[1,2,3,4,5]
dict1 = {}
print(f'list 1 contains keys {lst1}')
print(f'list 2 contains valuess {lst2}')
for i,j in zip(lst1,lst2):
    dict1[i]=j
print(f'Dict created using two lists {dict1}')
