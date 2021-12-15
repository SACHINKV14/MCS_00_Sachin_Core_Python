# Python program to find the largest
# number among the three numbers

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


# Driven code
a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))
print("maximum number is:",maximum(a, b, c))

print("-----------------------------------")
# Python program to find the largest number
# among the  three numbers using library function

def maximum1(a1, b1, c1):
    list1 = [a1, b1, c1]
    return max(list1)

# Driven code
a1 = int(input("Enter First Number:"))
b1 = int(input("Enter Second Number:"))
c1 = int(input("Enter Third Number:"))
print("maximum number is:",maximum1(a1, b1, c1))
print("-----------------------------------")
# Python program to find the largest number
# among the  three numbers using library function

# Driven code
# Driven code
a2 = int(input("Enter First Number:"))
b2 = int(input("Enter Second Number:"))
c2 = int(input("Enter Third Number:"))
print("maximum number is:",max(a2, b2, c2))