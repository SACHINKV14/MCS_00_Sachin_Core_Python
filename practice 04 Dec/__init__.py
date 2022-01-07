#learn to store the value
def caesr_encrypt(str1):
    s2 = ''
    for i in str1:
        i = ord(i) + 4
        s2 = s2.join(chr(i))
        s3 = s2,end=''
        print(s2,end='')
        print(f'caeser encrypted string is:{s3}')
    # print(s2)

str1=input("enter the input:")
caesr_encrypt(str1)
