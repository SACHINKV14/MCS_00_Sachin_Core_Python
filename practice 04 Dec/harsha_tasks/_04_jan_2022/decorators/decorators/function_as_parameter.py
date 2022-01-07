def function1():
    print("hi i am func1")
def function2(func):
    print("hi i am function 2 now i will call function1")
    func()

function2(function1) 