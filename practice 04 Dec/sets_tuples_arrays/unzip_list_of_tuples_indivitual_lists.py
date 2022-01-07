#create a tuple
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))
'''The zip() function pairs up the elements from all inputs,
 starting with the first values, then the second, etc. By using *l'''