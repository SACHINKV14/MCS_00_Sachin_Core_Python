class Strcount:
    def str_count(self,str1):
        count_alpha = 0
        count_number = 0
        for i in str1:
            if 'a' <= i <= 'z' and 'A' <= i <= 'Z':
                count_alpha += 1
            elif i.isnumeric():
                count_number += 1
        print(f'number of alpha characters is \"{count_alpha}\"')
        print(f'number of numbers in strings is \"{count_number}\"')

str1=input("Enter string here:")
a1=Strcount()
a1.str_count(str1)

