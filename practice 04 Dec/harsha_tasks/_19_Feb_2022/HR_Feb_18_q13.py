"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

"""
def swap_case(s):
    print(s)
    str1=""
    for i in s:
        if i.islower():
            str1+=i.upper()
        else:
            str1 += i.lower()
    return str1

if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)