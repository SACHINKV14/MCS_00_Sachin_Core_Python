my_list = [4, 7, 0, 3]        # 1. Define a list
my_iter = my_list.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())   #first element
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
# print(my_iter.__next__())  #gives error because index out of range
print("---------------------------------------------------------")
name='sachin'
name_iter = name.__iter__()  # 2. Get an iterator using iter()  OR   iter(my_list)
print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(name_iter.__next__())   #first element
print(name_iter.__next__())
print(name_iter.__next__())
print(name_iter.__next__())
print(name_iter.__next__())  #
print(name_iter.__next__())

print("----------------------")
print("set")
s1={1,2,3,4,5,6,7}
s1_iter=s1.__iter__()
print(s1_iter.__next__())   #first element
print(s1_iter.__next__())
print(s1_iter.__next__())
print(s1_iter.__next__())
print(s1_iter.__next__())  #
print(s1_iter.__next__())
print(s1_iter.__next__())


