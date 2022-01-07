#Add Items
#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print("-----------------------------------")
'''Add tuple to a tuple. You are allowed to add tuples to tuples, 
so if you want to add one item, (or many),
 create a new tuple with the item(s), and add it to the existing tuple:'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)