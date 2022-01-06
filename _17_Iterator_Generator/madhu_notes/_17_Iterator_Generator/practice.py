'''
iterator - combination __iter__ method and __next__method . fast result but memory wastage
generator - slow execution but good  memory management
'''

obj = ["even" if i % 2 == 0 else "odd" for i in range(10)]
print(obj)
list1 = []
for i in range(10):
    if i % 2 == 0:
        list1.append("Even")
    else:
        list1.append("Odd")
        print(list1)


list = [1, 2, 3]
square = [i*i for i in list]
print(square)

tuple = (1, 5, 6)
mulptiply = [i * 10 for i in tuple]
print(mulptiply)