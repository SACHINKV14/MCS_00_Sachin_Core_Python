#this is not
def Remove_space(string):
    return " ".join(string.split())


string = '''Lorem ipsum dolor sit amet,
    consectetur adipiscing elit,
    sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua.'''

String_without_space=Remove_space(string)
print(String_without_space)

