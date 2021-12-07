class Dictmap:
    def map_lists(self,lst1,lst2):
        dict1=dict(zip(lst1,lst2))
        print(f'Dict created using two lists {dict1}')


num=int(input('enter number of values for dict:'))
lst1=[]
lst2=[]
for i in range(num):
    l1=input('enter keys for dict:')
    lst1.append(i)
for j in range(num):
    l2 = input('enter values for dict:')
    lst2.append(l2)

print(f'list 1 contains keys {lst1}')
print(f'list 2 contains valuess {lst2}')
d1=Dictmap()
d1.map_lists(lst1,lst2)
