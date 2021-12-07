class Dictline:
    def print_dict_line(self,dict1):
        print("dict items line by line")
        for key in dict1.keys():
            print(f'key is {key}')
        for value in dict1.values():
            print(f'value is {value}')
        for item in dict1.items():
            print(f'item is {item} ')

dict1={'a':1,'b':2,'c':3}
d1=Dictline()
d1.print_dict_line(dict1)

print("------------------------------------------")
