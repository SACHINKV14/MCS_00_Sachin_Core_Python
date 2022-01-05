#y is global variable here
y=10  #defined begining of the script
def inner():
    x=4  #local variable

    print("inside func y=",y)
    print(x)

inner()

print("y",y)


print("-----------------------")
# y is global variable here
y = 10  # defined begining of the script


def inner():
    x = 4  # local variable
    y=5
    print("inside func y=", y)
    print(x)


inner()

print("y", y)

print("-----------------------")
#changing global var inside func
y=10
def inner():
    x = 4  # local variable
    global y  #use global keyword
    y=y+1
    print("inside func y=", y)
    print(x)

inner()

print("y", y)

print("-----------------------------")


