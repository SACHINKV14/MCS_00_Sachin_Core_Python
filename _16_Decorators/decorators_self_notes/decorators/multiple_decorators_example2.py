#convert string into upper case and split the string

#decorator func
def upr_d(func):
    def inner():
        str1=func()
        return "first "+func()+" first"
    return inner

def split_d(func):
    def wrapper():
        str2=func()
        return "second "+func()+"  second"
    return wrapper

@split_d
@upr_d      #firat decorator function
def ordinary():
    return "good morning"

print(ordinary())



