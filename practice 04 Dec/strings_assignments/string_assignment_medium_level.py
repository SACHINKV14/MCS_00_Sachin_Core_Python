#39 reverse a string
def rev_str(str1):
    print(f'reversed string is :{str1[::-1]}')

#64 Reverse a given string  Input : "Python"   Output : "nohtyP"
def rev_str1():
    str10 = 'Python'
    print(f'reversed string is :{str10[::-1]}')

#67 that accepts a string and calculate the number of digits and letters
def count_num_char():
    str11 = input("enter string with alphanumreic:")
    count_num = 0
    count_char = 0
    for i in str11:
        if i.isnumeric():
            count_num += 1
        elif i.isalpha():
            count_char += 1
    print(f'number of characters is :{count_char}\nnumber of digits is:{count_num}')

#65 Reverse each word in given string Input
def rev_str_input():
    str12 = input("enter string:")
    print(f'reversed string is :{str12[::-1]}')

#45 check if a string contains all letters of the alphabet
def str_all_alphabets(str1):
    # str15 = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    # str15 = str15.split(",")
    # print("above or below")
    str15 = 'abcdefghijklmnopqrstuvwxyz'
    for a in str15:
        if a not in str1:
            print(f'{a} is not there in string')
        else:
            print(f'{a} present in string')

#25 program to create a Caesar encryption
#learn to store the value
def caesr_encrypt(str1):
    s2 = ''
    for i in str1:
        i = ord(i) + 4
        s2 = s2.join(chr(i))
        print(f'caeser encrypted string is:{s2,end=''})
    # print(s2)

#5 Swapping chars in string
def swap_chars(str1):
    str1 = str1.lower()
    str1 = str1.replace("s", "*")
    str1 = str1.replace("a", "s")
    str1 = str1.replace("*", "a")
    print(str1)

#14 sort words alphanumerically
def sort_alphanum(str1):
    lst = str1.split()
    lst2 = list(sorted(lst))
    # print(lst2)
    #join without spaces
    str_sorted = "".join(lst2)  #if we give empty string it will join without spaces
    print(str_sorted)
    #join with the spaces
    str_sort=" "                #if we give space string it will join with spaces
    print(str_sort.join(lst2))

#28 to add a prefix text to all of the lines in a string
def add_prefix(str_pre):
    lst1 = str_pre.split("\n")
    print(lst1)
    str5 = '@#$%^'
    print(f'string with addeed prefix to each line:')
    for a in lst1:
        print(str5 + a)

#62 sum of digits in a string
def sum_digit(str1_digit):
    count_digit = 0
    for i in str1_digit:
        if i.isnumeric():
            count_digit += 1
    print(f'Number of digits in a given string is:{count_digit}')

#65 Reverse each word string Input
def rev_str_word_input(str_word):
    str1 = str_word.split()
    b=[]
    for a in str1:
        b.append(a[::-1])
    str3 = " ".join(b)
    print(f'reversed string is :{str3}')

#65 Reverse each word string Input
def rev_str_word(str_rev_word):
    str1 = str_rev_word.split()
    b=[]
    for a in str1:
        b.append(a[::-1])
    str3 = " ".join(b)
    print(f'reversed word string is :{str3}')

#66 Reverse each word and reverse word again. Input
def rev_str_word_input_to_get_original(str_word1):
    str1 = str_word1.split()
    b=[]
    for a in str1:
        b.append(a[::-1])
    str3 = " ".join(b)
    print(f'reversed string is :{str3}')
    str4 = str3.split()
    b1 = []
    for a1 in str4:
        b1.append(a1[::-1])
    str5 = " ".join(b1)
    print(f'getting original string from reversed string is :{str5}')

str1='A quick brown fox jumps over the lazy dog'

#39 reverse a string
# rev_str(str1)
#
# #64 Reverse a given string  Input : "Python"   Output : "nohtyP"
# rev_str1()

# #67 that accepts a string and calculate the number of digits and letters
# count_num_char()

# #65 Reverse each word in given string Input
# rev_str_input()

# #65 Reverse each word in given string Input
# rev_str_input()

# #45 check if a string contains all letters of the alphabet
# str_all_alphabets(str1)

# #25 program to create a Caesar encryption
# caesr_encrypt(str1)

# #5 Swapping chars in string
# swap_chars(str1)

# #14 sort words alphanumerically
# sort_alphanum(str1)
#

# #28 to add a prefix text to all of the lines in a string
# str_pre = '''A quick
# brown fox
# jumps over
# the lazy dog'''
# add_prefix(str_pre)

# #62 sum of digits in a string
# str1_digit='jbhbfkjbkh8546939625'
# sum_digit(str1_digit)

# #65 Reverse each word string Input
# str_word = input("enter string:")
# rev_str_word_input(str_word)

# #66 Reverse each word and reverse word again. Input
# str_word1 = input("enter string:")
# rev_str_word_input_to_get_original(str_word1)

#40 reverse words in a string
str_rev_word = input("enter string:")
rev_str_word(str_rev_word)

