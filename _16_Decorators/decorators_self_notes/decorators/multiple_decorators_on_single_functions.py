#convert string into upper case and split the string

#decorator func
def upr_d(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return str2.split()
    return wrapper

#if we interchange the decorators we will get error
#because cant apply upper function on list
@split_d
@upr_d      #firat decorator function
def ordinary():
    return "good morning"

print(ordinary())



