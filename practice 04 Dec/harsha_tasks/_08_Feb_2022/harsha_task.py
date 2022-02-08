"palindromic number"
import itertools
from itertools import permutations
def palindromes(lst):
    results=[]
    for text in lst:
        if text == text[::-1]:
            results.append(text)
    return results

# text="2341"
text="388003"
lst=[]
perm = itertools.permutations(text,len(text))
for i in perm:
    a=list(i)
    str1="".join(a)
    lst.append(str1)

res = set(palindromes(lst))
if len(res)==0:
    print(-1)
else:
    print(max(res))
