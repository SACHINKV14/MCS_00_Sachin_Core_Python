#general decorator func can be used on many functions

def div_decorator(func):
    def inner(*args):  #to use mutiple arguments
        list1=[]
        list1=args[1:]  #after first arg shd not be eqaul to zero
        for i in list1:
            if i==0:
                return "give proper input!!!"
        return func(*args)
    return inner

@div_decorator
def div1(a,b):
    return a/b

@div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(10,0))
print(div2(10,9,5))