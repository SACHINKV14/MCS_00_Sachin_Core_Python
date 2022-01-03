
# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci( n -1) + recursive_fibonacci( n -2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
    for i in range(n_terms):
        print(recursive_fibonacci(i))

print("--------------")
x=5
lst=[0,1]
for i in range(3,x+1):
    b=lst[-1]+lst[-2]
    lst.append(b)

# print(lst)