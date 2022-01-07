# 2. NESTED FUNCTIONS :
print("---------------2. NESTED FUNCTIONS------------------")


def some_fin():
    return 'harsha'
name = some_fin
print(name)
def parent():
    print("Before Nested Function")

    def first_child():  # nested function

        def new_func():
            print('..........................')
            return 'In new nest func'

        return new_func
    print("After Nested Function")

    print("Inside parent :", first_child())
    print("Inside parent :", first_child)

    return first_child  # <function parent.<locals>.first_child at 0x000001B0034A3BF8>

a = parent()()()
print(a)

# print(parent.first_child())
f_child = parent()
# this is going to make copy of first_chil
print("Outside parent :", f_child())
print("Outside parent :", f_child)


# parent.first_child()  # It gives error
# parent.first_child()  This is not the way to call nested function

print("Parent function address: ", parent)  # parent = <function parent1 at 0x000001BF373B1E18>   x = 10

print("---Parent function call :-----")
print(parent())
print('-----------------------------')
# a = sum  return a + b
nest_func_addr = parent()  # chil_func
print(nest_func_addr)
print('..............................')
print("Calling  nested function from outside function      : ", nest_func_addr())  # 12 line
print("Printing nested function name from outside function : ", nest_func_addr)    # 13 line

print("------Using EXCEPTION HANDLING ---------------- ")
try:
    #parent.first_child()
    f_child = parent()  #
    print("Calling child function : ", f_child())
except AttributeError as err:
    print("Exception :: ", err)
    print("--You cannot call nested function directly------")


print("---------------------------------------------------")