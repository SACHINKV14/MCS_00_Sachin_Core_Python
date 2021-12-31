class String:
    def move_spaces(self,str1):
        count = str1.count(" ")
        print(f'number of spaces is:{count}')
        str1 = " " * count + str1.replace(" ", "")
        print(f'string after removing spaces to front of the string:\n{str1}')

str1='A quick brown fox jumps over the lazy dog'
s1=String()
s1.move_spaces(str1)
print("--------------------------------")