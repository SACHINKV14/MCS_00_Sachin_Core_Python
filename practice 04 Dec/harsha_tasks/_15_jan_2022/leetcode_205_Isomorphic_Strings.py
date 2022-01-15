"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true

"""
# s = "egg"
# t = "add"

# s = "foo"
# t = "bar"

s = "paper"
t = "title"


if len(s)!=len(t):
    print("False")

elif len(s)==len(t):
    lsts=[]
    lstt=[]
    for i in s:
        if i not in lsts:
            lsts.append(i)
    for j in t:
        if j not in lstt:
            lstt.append(j)
    dict1 = {x:y for (x, y) in zip(lsts, lstt)}
    s1=s
    for k,y in dict1.items():
        s1=s1.replace(k,y)
    if s1 == t:
        print("True")
    else:
        print("False")


