"that accepts a string and calculate the number of digits and letters"

str1=input("enter  a string:")
count_number=0
count_alpha=0
try:
    for i in str1:
        if 'a' <= i <= 'z' and 'A' <= i <='Z':
            count_alpha += 1
        elif i.isnumeric():
            count_number += 1
        else:
            raise ValueError
    print(f'number of alpha characters is \"{count_alpha}\"')
    print(f'number of numbers in strings is \"{count_number}\"')

except ValueError as e:
    print('do not enter special character')




