# Python program to print all
# prime number in an interval
# number should be greater than 1


def prime_num(start,end):
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if (i % j == 0):
                    break
            else:
                # print(f' prime numbers : {i} ')
                prime_numbers.append(i)
    print(f' prime numbers within {start},{end} : {prime_numbers} ')


start = int(input("enter starting number:"))
end = int(input("enter ending number:"))
prime_numbers=[]
prime_num(start,end)