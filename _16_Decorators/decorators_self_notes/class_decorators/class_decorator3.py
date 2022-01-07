class Check_div:
    def __init__(self,func ):
        self.func=func
    def __call__(self, *args, **kwargs):
        if args[1] == 0:
            return "You can't devide change the input!"
        else:
            return self.func(*args,**kwargs)

@Check_div
def div(a,b):
    return a/b
@Check_div
def div1(a,b,c):
    return a/b/c

print(div(10,10))
print(div(10,0,5))