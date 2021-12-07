class Dictline:
    def print_dict_line(self,dict1):
        print("dict items line by line")
        for i in dict1.items():
            print(i)

dict1={'a':1,'b':2,'c':3}
d1=Dictline()
d1.print_dict_line(dict1)