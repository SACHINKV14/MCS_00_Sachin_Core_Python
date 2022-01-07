y=10
def outer():
    z = 4  # local variable
    def inner():
        x=4
        print("x:",x)
        print("inside func y=", y)
    inner()
    print("z:",z)

outer()


#z local to outer function and nonlocal to inner function
#z is the enclosing variable
#z canoot access by outside the outer function or inside the inner function


print("-----------------------")
#modify the enclosinjg variable inside local sco[pe
y=10
def outer():
    z = 4  # local variable
    def inner():
        x=4
        nonlocal z    #nonlocal keyword to modify
        z =z+1
        print("x:",x)
        print("inside func y=", y)
    inner()
    print("z:",z)

outer()