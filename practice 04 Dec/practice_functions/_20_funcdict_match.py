dict1 = {'a': 1, 'c': 3, 'b': 2}
dict2 = {'a': 1, 'b': 2}

for (key, value) in set(dict1.items()) & set(dict2.items()):
    print(' present in both dict1 and dict2 is:{%s: %s}' % (key, value))
