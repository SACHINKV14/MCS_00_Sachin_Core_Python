import textwrap

def wrap(string, max_width):
    lst=[]
    for i in range(0,len(string),3):
        lst.append(string[i:i+3])
    return lst

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string="ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    max_width=4
    result = wrap(string, max_width)
    for i in result:
        print(i)

print("-----------------------------")
# import textwrap
#
#
# def wrap(string, max_width):
#     return textwrap.fill(string, max_width)
#
#
# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)