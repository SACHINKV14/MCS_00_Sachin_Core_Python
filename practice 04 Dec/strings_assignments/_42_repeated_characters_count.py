import collections

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
frequencies=collections.Counter(a)
repeated={}
for key,value in frequencies.items():
    if value>1:
        repeated[key]=value
print(repeated)