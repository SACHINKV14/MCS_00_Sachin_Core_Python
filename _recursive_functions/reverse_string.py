def rev_str(str):
    if len(str)==0:
        return str
    else:
        return rev_str(str[1:])+str[0]

str1='sachin'
print(f'original string {str1}')
r_str=rev_str(str1)
print(f'reversed string is:{r_str}')
