# Python Program to Calculate Cube of a Number

def square_cube(num):
    square_num=num*num
    cube_num=num*num*num
    return square_num,cube_num

number = float(input(" Please Enter any numeric Value : "))

n_square,n_cube = square_cube(number)

print("The Square of a Given Number {0}  = {1}".format(number, n_square))
print("The Cube of a Given Number {0}  = {1}".format(number, n_cube))