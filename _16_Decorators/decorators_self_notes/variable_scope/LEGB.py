x=5
def function():
    x=10
    def inner():
        x=15
        print("x:",x)
    inner()
function()