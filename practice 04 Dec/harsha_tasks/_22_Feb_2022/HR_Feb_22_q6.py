import string
def print_rangoli(size):
    n = size
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(chr(65 + k), end='')
        print()



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
