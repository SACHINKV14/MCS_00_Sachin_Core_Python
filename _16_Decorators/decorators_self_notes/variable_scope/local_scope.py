#local : contains names defind inside the current function
def inner():   #global func variable(bcz present at begining of func)
    x=4  #defined inside the func its a local var(scope of this is inside the function)
    print(x)
inner()

print(x)  #gives name error