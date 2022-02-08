"""
Task
You are given a string.
Split the string on a " " (space) delimiter and join using a - hyphen.
"""

def split_and_join(line):

    # write your code here
    lst=line.split(" ")
    str1="-".join(lst)
    return str1

if __name__ == '__main__':
    line = "this is a string"
    # line = input()
    result = split_and_join(line)
    print(result)