str1="welcome to python"
lst=[]
for i in str1.split():
    lst.append(i[::-1])
s2=" ".join(lst)
print(s2)