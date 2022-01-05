def outer():
    x=3
    def inner():
        print(x)
    return inner() #not value return func so it returns none

a=outer()
print(a)

print("---------------------------------")
#to return values
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner()

a=outer()
print(a)

print("--------------------------")

#to return inner function reference
def outer():
    x=3
    def inner():
        y=3
        result=x+y
        return result
    return inner

a=outer()
print(a)
print(a.__name__) #name of the function



