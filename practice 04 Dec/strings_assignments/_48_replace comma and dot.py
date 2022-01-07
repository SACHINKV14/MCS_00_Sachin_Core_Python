
def Replace(a):
    a = a.replace(',','#')
    a = a.replace('.',',')
    a = a.replace('#','.')
    return a

a = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

print(a)
a_str=Replace(a)
print(a_str)