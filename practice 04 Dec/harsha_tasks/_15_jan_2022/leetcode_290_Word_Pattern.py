"""
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty word in s.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
# pattern = "abba"
# s = "dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat fish"

pattern = "aaaa"
s = "dog cat cat dog"

lsti=[]
for li in pattern:
    if li not in lsti:
        lsti.append(li)
lsts=[]
for si in s.split(" "):
    if si not in lsts:
        lsts.append(si)
if len(lsts)!=len(lsts):
    print("False")

elif len(lsts)==len(lsts):
    dict1={y:x for (x,y) in zip(lsti,lsts)}
    s1 = s.replace(" ", "")
    for i3 in dict1.keys():
        s1=s1.replace(i3,dict1[i3])
        # print(s1)
    if s1==pattern:
        print("True")
    else:
        print("False")
