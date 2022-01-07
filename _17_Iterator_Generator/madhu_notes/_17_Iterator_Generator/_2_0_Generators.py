
# https://www.programiz.com/python-programming/generator#:~:text=Python%20generators%20are%20a%20simple,one%20value%20at%20a%20time).
# https://www.programiz.com/python-programming/generator
'''
Python 2.x
--------------
range  - Iterator   -- Speed of execution
xrange - Generator  -- Memory management
    
Python 3.x 
-----------
range  - Generator
range(10)

What are generators in Python?
 => There is a lot of overhead in building an iterator in Python
    We have to implement a class with __iter__() and __next__() method,
    keep track of internal states,raise StopIteration when there was no values to be returned etc.
    This is both lengthy and counter intuitive.
  
 => Generator comes into rescue in such situations.
 => Python generators are a simple way of creating iterators
     All the overhead we mentioned above are automatically handled by generators in Python.
=> A generator is a function that returns an object (iterator) which we can iterate over (one value at a time).

How to create a generator in Python?

=> It is fairly simple to create a generator in Python. 
=> It is as easy as defining a normal function with yield statement instead of a return statement.

=> If a function contains at least one yield statement (it may contain other yield or return statements), it becomes a generator function. 
   Both yield and return will return some value from a function.

=> The difference is that, while a return statement terminates a function entirely, yield statement pauses the function saving all its states and 
   later continues from there on successive calls.
'''
def some_fun():
    i = 0
    while True:
        i += 1
        if i > 100:
            break
        return i
# 1 --101
print('.....',some_fun())  # 1

    # [1 :10:2]
def some_fun():
    i = 0
    while True:
        i += 1 # 3
        print('new line')
        if i > 100:
            break
        yield i
# for num in [1,2,3,4]:
#     print(num)
#
# #1 2 3
# for num in some_fun():
#     print(num)
#
a = some_fun()
print(a)
print('.........NEXT USING GENERATOR',next(a))
print('.........NEXT USING GENERATOR    AGAIN:',next(a))

def even_num(num =0):

    while True:
        if num %2 == 0:
            yield num
        num += 1

a = even_num()
print('first even number ',next(a))  # 0
print('second even number ',next(a))  # 2

# for a in even_num():
#     print(a)  # 0 2 4 6 8
'''
Generators in Python :
=======================
There is a lot of work in building an iterator in Python. 
We have to implement a class with __iter__() and __next__() 
method, keep track of internal states, and raise StopIteration when there are no values to be returned.

This is both lengthy and counter intuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. 
All the work we mentioned above are automatically handled by  generators in Python.

Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over 
(one value at a time).
'''
#Iterator

class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        print(result)

pow = PowTwo(3)
pow.__next__()
pow.__next__()
pow.__next__()

print("-----------Generator Function-------------")

def pow_two_gen(max=0):
    n = 0 # n =1
    while n < max:  # 0 < 3
        yield 2 ** n  # 1
        n += 1   # n = 1

for each in pow_two_gen(3):
    print(each)   # 1


a = pow_two_gen(3)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

print("-----------Generator Function-------------")

def pow_two_gen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
for each in pow_two_gen(3):
    print(each)
    pass
