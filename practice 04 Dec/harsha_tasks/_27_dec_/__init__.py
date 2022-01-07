# a=['a','b','c','d','e','f']
a=[1,2,3,4,5,6]
count=10
split_index = (count % len(a) - 1)
print(count%len(a))
print(a[count%len(a)])
print(split_index)
print(a[split_index])
