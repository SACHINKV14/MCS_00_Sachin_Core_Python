"""
The first line of input contains the original string. The next line contains the substring.
Output the integer number indicating the total number of occurrences of the substring in the original string.
"""
# ip="ABCDCDC"
# # op="CDC"

ip = "AbcdAbcdAbcdAbcd"
op = "Ab"
count=0
num=0
while num<len(ip):
    a=ip.find(op)
    if a>0:
        count+=1


    if ip.find(op,a,len(op)+1):
        ip=ip.replace(op[0],"*",1)
        num+=1

print(count)
