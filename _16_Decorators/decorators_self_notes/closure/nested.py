def outer(): #func def(enclosing func)
    x=3
    def inner(): #func def(nested func)
        print(x)
    inner()

outer()