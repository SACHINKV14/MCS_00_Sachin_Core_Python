"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""
def timeConversion(s):
    # Write your code here
    if s[0:2]!='12' and s[-2::]=="PM":
        a=int(s[0:2:1])+12
        a=str(a)+s[2:-2]
        return a
    elif s[0:2]=='12' and s[-2::]=="PM":
        a=s[0:-2:]
        return a
    elif s[0:2]=='12':
        a='00'+s[2:-2]
        return a

    else:
        a=s[0:-2]
        return a

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
