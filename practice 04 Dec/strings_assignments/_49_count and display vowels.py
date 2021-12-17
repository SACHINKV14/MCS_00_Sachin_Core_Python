
a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

list1=['a','e','i','o','u']
a_lower=a.lower()
print(a_lower)
for i in list1:
    for j in a:
        pass
    print(f'occurances {i} is", {a_lower.count(i)}')

print('\n', a_lower.count('u'))