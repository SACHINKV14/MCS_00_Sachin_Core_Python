'''elements in set datatypes can be modified but not in frozensets
update and remove method not work on frozenset so they canot be modified or update'''

s={10,20,30,40,50}
print(f'set is:{s}')

fs=frozenset(s)
print(f'frozen set is:{fs}')

print("----------------------------")
fs1=frozenset("sachin")
print(f'frozen set from stringis:{fs1}')