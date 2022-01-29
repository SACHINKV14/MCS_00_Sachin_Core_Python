"""Task
Given an integer, , perform the following conditional actions
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""
if __name__ == '__main__':
    n = int(input("enter number:").strip())
    if n%2==0:
        if n>=2 and n<=5:
            print("Not Weird")
        if n>=6 and n<20:
            print("Weird")
        if n>=20:
            print("Not Weird")
    else:
        print('Weird')