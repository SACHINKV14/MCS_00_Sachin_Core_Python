"""
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2
"""
def swap_case(s):
    lst=[]
    for i in s:
        if i.islower():
            lst.append(i.upper())
        elif i.isupper():
            lst.append(i.lower())
        else:

            lst.append(i)
    str1="".join(lst)
    return str1

if __name__ == '__main__':
    s = input("enter string:")
    result = swap_case(s)
    print(result)