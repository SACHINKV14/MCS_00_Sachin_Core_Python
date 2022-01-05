def outer(expr):
    def upr_d(func):
        def inner():
            return func()+expr
        return inner
    return upr_d

@outer(" sachin")
def ordinary():
    return "good morning"

print(ordinary())


 
