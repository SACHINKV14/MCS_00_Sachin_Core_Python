"""Task
The provided code stub reads and integer, , from STDIN.
For all non-negative integers , print .
"""
if __name__ == '__main__':
    n = int(input("enter the number:"))
    for i in range(n):
        print(i*i)
