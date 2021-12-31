'''420. Strong Password Checker
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
'''
flag=True
while(flag):
    password=input("enter password:")
    s_char='[@_!#$%^&*()<>?/\|}{~:]_+":;'
    if len(password)<6 or len(password)>20:
        print("password length should be min:6,max:20 chars")
        continue
    else:
        flag = False
cl = cu = cd = cs = 0
for i in password:
    if i.islower():
        cl += 1
    elif i.isupper():
        cu += 1
    elif i.isnumeric():
        cd += 1
    elif i in s_char:
        cs += 1

if cl>=1 and cu>=1 and cd>=1 and cs>=1:
    print('\"entered password is strong\"')
if cl==0:
    print("add lower case to make your password strong")
if cu==0:
    print("add upper case to make your password strong")
if cd==0:
    print("add digit to make your password strong")
if cs==0:
    print("add special character to make your password strong")

