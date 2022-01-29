"""Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines.
The first line should contain the result of integer division,  // .
The second line should contain the result of float division,  / .

No rounding or formatting is necessary.
"""
if __name__ == '__main__':
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    print(a//b)
    print(a/b)
