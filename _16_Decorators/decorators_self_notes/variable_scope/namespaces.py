#dir() is used to see the names

print("initially",dir())
num=20
def f1():
    n=10
    print("inside the function:",dir())
print("outside the function:",dir())
f1()