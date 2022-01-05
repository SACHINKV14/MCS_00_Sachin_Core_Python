def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner

a=outer()
print(a())

#executing inner func outside its scope the func is called as closure


print("------------------")

def outer():
    msg='hello'
    def inner():
        print(msg)
    return inner

a=outer()
a()
