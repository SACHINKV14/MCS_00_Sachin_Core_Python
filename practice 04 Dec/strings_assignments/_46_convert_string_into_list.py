def convert_to_list(string):
    list1=list(string.split(" "))
    return list1

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''

list_converted=convert_to_list(a2)
print(list_converted)


#remove new lines \n in strings