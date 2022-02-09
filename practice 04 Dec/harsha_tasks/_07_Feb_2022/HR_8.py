"""
The first line of input contains the original string. The next line contains the substring.
Output the integer number indicating the total number of occurrences of the substring in the original string.
"""
# ip="ABCDCDC"
# op="CDC"

ip = "AbcdAbcdAbcdAbcd"
op = "Ab"

# ip="ininini"
# op="ini"
# count=0
# num=0
# while num<len(ip):
#     a=ip.find(op)
#     if a>0:
#         print(a)
#         count+=1
#     if ip.find(op,a,len(op)+1):
#         ip=ip.replace(op[0],"*",1)
#         num+=1

print("-------------------Method2-------------------------")
string=ip
sub_string=op
count=0
for i in range(len(string)):
    if string[i:i+len(sub_string)]==sub_string:
        count+=1
    # return count

print(count)
