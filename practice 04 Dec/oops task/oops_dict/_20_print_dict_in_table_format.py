class Dicttable:
    def dict_print_table(self,dict1):
        print('Name', '\t', 'jersey number')
        for (x1, x2) in zip(dict1.keys(), dict1.values()):
            print(x1, '\t', x2)

dict1={'sachin':10,'virat':18,'dhoni':7}
a1=Dicttable()
a1.dict_print_table(dict1)

print("------------------------------------------")

# print("----------not working---------------------")
# from tabulate import tabulate
# print(tabulate([[dict1.keys(),dict.values()]], headers=['Name', 'Age']))
# print("----------not working---------------------")

print("------------------------------------------")
'''Python allows us to perform efficient string-formatting using the format() function. It gives us the freedom to make sure we get the output in our desired format.

For showing data in a tabular format, we specify the spaces efficiently between the columns and print the data from the list in the same format.

For example,'''


print("{:<8} {:<15}" .format('Name','Jercy number'))

for x, y in dict1.items():
    print("{:<8} {:<15}".format(x,y))

print("------------------------------------------")






























# ################3https://www.geeksforgeeks.org/python-program-to-print-the-dictionary-in-table-format/