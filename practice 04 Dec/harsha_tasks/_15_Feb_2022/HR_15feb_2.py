"""
A single line of input containing the full name, .
"""
def solve(s):
    lst=[]
    for i in s.split():
        a=i.capitalize()
        lst.append(a)
    str1=" ".join(lst)
    print(str1)


# s="chris alan"
s="12abc"
# s="132 456 Wq m e"
solve(s)

