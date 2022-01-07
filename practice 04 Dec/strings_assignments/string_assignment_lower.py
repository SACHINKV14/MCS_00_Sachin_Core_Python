#1 to find length of a string fun def
def len_str(str1):
    print(f'length of the string is: {len(str1)}')
#2 to number of chars in string func call
def count_char(str1):
    print(f'length of only characters in strings: {len(str2)}')
#3 string slicing func def
def str_slice(str1):
    print(f'sliced string in \"{str1}\" is \"{str1[0:10]}\"')
#8 longest word in string func def
def long_string(str3):
    print(f'maximum length of a string based on length is :{max(str3, key=len)}')   #string has many words with same length but it prints only onw word highest alphabet char

#10 swaping first and last case of string
def swap_fl(str1):
    print(f'original string is :\n \t{str1}\nswapped string of first and last string is:\n \t{str1[-1]+str1[1:-1]+str1[0]}')

#11 remove odd index values of string func call
def removed_odd_index(str1):
    print(f'string after removing odd indexes is:{str1[1::2]}')

#12 Count words in a string
def count_words(str1):
    str1 = str1.replace(",", " ")
    str1 = str1.replace("\n", " ")
    str1 = str1.replace("\t", " ")
    # print(str1)
    str1.split()
    print(f'number of words in the string is :{len(str1.split())}')

#21 convert str to upper case
def str_upper(str1):
    print(f'string upper case:{str1.upper()}')

#24 to check string starts with paricular char
def str_start_with_particualr_char(str1):
    str1 = str1.lower()
    start_string = input('enter the letter which u want to check string start with:').lower()
    if str1[0] == start_string:
        print(f'string starts with the \"{start_string}\" character.')
    else:
        print(f'string not starts with the \"{start_string}\" character.')

#44 print the index of the character in a string
def char_index(str1):
    str1 = str1.lower()
    char1 = input('enter the char to find its index in string:').lower()
    print(f'\"{char1}\" present in string at {str1.find(char1)} index')

#46 convert string into a list
def str_to_lst(str1):
    str1 = str1.replace(",", " ")
    str1 = str1.replace("\n", " ")
    str1 = str1.replace("\t", " ")
    print(f'string into a list is :{str1.split()}')

#57 remove spaces from given string
def str_reomve_space(str1):
    print(str1.replace(" ", ""))

#60 capitalize first and last word
def str_capital_f_l():
    txt1=input("Enter text here:")
    for word in txt1.split():
        a1 = word[0].capitalize() + word[1:-1] + word[-1].capitalize()
        print(a1,end=" ")

#49 count vowels in a string
def count_vowels(str1):
    lst1 = ['a', 'e', 'i', 'o', 'u']
    str1 = str1.lower()
    print(f'string is:{str1}')
    for i in lst1:
        print(f'occurances {i} is:, {str1.count(i)} times')

#48 swap comma and dot
def swap_comma_dot():
    str10 = 'sachin,is good.'
    str10 = str10.replace(".", "*")
    str10 = str10.replace(",", ".")
    str10 = str10.replace("*", ",")
    print(str10)

str1 = "A quick brown fox jumps over the lazy dog"

# #1 to find length of a string func call
# len_str(str1)

# #2 to number of chars in string func call
# str2 = str1.replace(" ","")
# count_char(str2)
#
# #3 string slicing func call
# str_slice(str1)
#
# # 8 longest string in python func call
# str3 = str1.split()
# long_string(str3)
#
# #10 first and last character swap
# swap_fl(str1)
#
# #11 remove odd index values of string func call
# removed_odd_index(str1)

# #12 count words in string
# count_words(str1)
#

# #21 convert str to upper case
# str_upper(str1)

# #24 to check string starts with paricular char
# str_start_with_particualr_char(str1)

# #44 print the index of the character in a string
# char_index(str1)

# #46 convert string into a list
# str_to_lst(str1)

# #57 remove spaces from given string
# str_reomve_space(str1)

# #60 capitalize first and last word in string
# str_capital_f_l()

# #49 count vowels in a string
# count_vowels(str1)

# #48 swap comma and dot
# swap_comma_dot()
#

