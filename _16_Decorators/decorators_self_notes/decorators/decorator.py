#decorator function
def str_upr(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner    #func reference

def print_str():
    return "good morning"

print(print_str())

d = str_upr(print_str)    #=  @decorator func name
print(d())


print("---------------------")
#decorator function
def str_upr(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner    #func reference

@str_upr
def print_str():    #not contains any parameter
    return "good morning"

print(print_str())