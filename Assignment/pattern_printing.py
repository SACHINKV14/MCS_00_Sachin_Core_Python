# n=int(input("enter value :"))
#
# for i in range(a+1):
#     for j in range(i):
#         print("*",end=" ")

# n=int(input("enter value :"))
# i=1
# for i in range(n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print("\n")

# n=int(input("enter value :"))
# i=1
# for i in range(n+1):
#     for j in range(i):
#         print(j,end=" ")
#     print("\n")

# n=int(input("enter value :"))
# i=n-1
# for i in range(n):
#     for j in range(n-1):
#         print(" ",i)
#     print("\n")

# a='♥'
# num=int(input("Enter number:"))
# for i in range(num+1):
#      for j in range(1,i+1):
#          print("♥",end="")    #end to print  symbol in side by side
#      print()

# a='♥'
# num=int(input("Enter number:"))
# for i in range(num,0,-1):
#      for j in range(i):
#          print("♥",end="")    #end to print  symbol in side by side
#      print()

'''This type of pyramid is a bit more complicated than the ones we studied above.

The outermost loop starts from i = 1 to i = row + 1.
Among the two inner loops, the for loop prints the required spaces for each row using formula (rows-i)+1, where rows is the total number of rows and i is the current row number.
The while loop prints the required number stars using formula 2 * i - 1. This formula gives the number of stars for each row, where row is i.'''

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("♥", end="")
        k += 1

    k = 0
    print()