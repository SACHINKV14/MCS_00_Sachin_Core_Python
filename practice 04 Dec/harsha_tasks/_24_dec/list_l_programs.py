#7 Remove duplicates in lists
def remove_duplicate(lst7):
    lst71=[]
    for i7 in lst7:
        if i7 not in lst71:
            lst71.append(i7)
    print(f'list after removing duplicates: {lst71}')

lst7=[1,2,3,4,5,6,7,8,9,5,6,7,4,3,2,1]
print(f'original list is: {lst7}')
remove_duplicate(lst7)

print("------------------------------------------------")
#8 Check list is empty or not
def list_empty(lst8):
    if len(lst8) == 0:
        print(f'list is empty')
    else:
        print("list is not empty")

# lst8=[]
lst8=[1,2,3]
list_empty(lst8)
print("------------------------------------------------")
#9 Clone or copy




print("------------------------------------------------")
#11 Find common element from 2 lists
lst111=[1,2,3,4,5,6]
lst112=[5,6,7,8,9,1]
res_lst11=[]
for i11 in lst111:
    if i11 in lst112:
        res_lst11.append(i11)
print(f'elements in both the lists are:{res_lst11}')
print("------------------------------------------------")

#12 Remove specified index from list and print
lst12=[9,8,7,6,5,4,3,2,1]
print(f'list before removing one element:{lst12} ')
num12 =int(input("enter the index u want to remove:"))
print(f'removed element at index {num12} in list is:{lst12.pop(num12)} ')
print(f'list removing  one index:{lst12} ')

# print("------------------------------------------------")
#14 Remove even elements and print list

# print("------------------------------------------------")
#15 Shuffle list and print

# print("------------------------------------------------")
#19 Difference betweeen 2 lists

# print("------------------------------------------------")
#20 To access index of list

# print("------------------------------------------------")
#21 List of characters into string
lst21=['s','a','c','h','i','n']
str21=""
for i21 in lst21:
    str21+=i21
print(f'string from list of chars is: {str21}')

# print("------------------------------------------------")
#14 Remove even elements and print list
lst14=[1,2,3,4,5,6,7,8,9,10,'s','a','c','h','i','n']
print(f'original list is:{lst14}')
for i14 in lst14[1::2]:
    lst14.remove(i14)
print(f'list after removing even placed values:{lst14}')
# print("------------------------------------------------")
#15 Shuffle list and print
import random
lst15=[1,2,3,4,5,6,7,8,9,10,'s','a','c','h','i','n']
print(f'before shuffling the list:{lst15}')
random.shuffle(lst15)
print(f'after shuffling the list:{lst15}')
# print("------------------------------------------------")

#24Append a list to second list
lst241=[1,2,3,4,5,6,7,8,9]
print(f'list 1 is:{lst241}')
lst242=['a','b','c','d','e']
print(f'list 2 is:{lst242}')
lst241.append(lst242)
print(f'appending list 2 to list 1 is:{lst241}')

# print("------------------------------------------------")

#68 Extend a list without append
lst681=[1,2,3,4,5,6,7,8,9]
print(f'list 1 is:{lst681}')
lst682=['a','b','c','d','e']
print(f'list 2 is:{lst682}')
lst681.extend(lst682)
print(f'appending list 2 without using appending to list 1 is:{lst681}')
# # print("------------------------------------------------")
#22 Finding index of an item in specified list
lst22=[1,2,3,4,5,6,7,8,9]
print(lst22.index(3))
# # print("------------------------------------------------")
#31 Counting number elementswithin a specified ranges
lst31=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,10,11,12,13,14]
count31=0
for i31 in lst31:
    if 1<=i31<=2:
        count31 += 1
print(f'number of elements within a range is:{count31}')
# # print("------------------------------------------------")
#32 Check a list contains sublist
lst32=[1,2,3,[4,5],'a',True,12.4]
# lst32=[1,2,3,'a',True,12.4]
count32=0
for i32 in lst32:
    if type(i32)==list:
        count32+=1
if count32==0:
    print(f'list contains zero sublist')
else:
    print(f'list conatains {count32} sublists')

# # print("------------------------------------------------")
#33 Generate all sublists
num33=int(input('enter legnth of lists:'))
lst33=[[x33,x33*x33] for x33 in range(num33+1)]
print(f'generated sublist is:{lst33}')
# # print("------------------------------------------------")
#34 Printing elements in ascending order
#sort requires homogenious data types
# lst34=[5,8,1,9,2,0,2,7,6,5,4]
lst34=['s','z','a','g','W','A']
lst34.sort(reverse=False)
print(lst34)
# # print("------------------------------------------------")
#44 Generate group of five consecutive numbers in a list
num44=int(input('enter strating number:'))
lst441=[]
for i441 in range(num44,num44+5):
    lst441.append(i441)
print(f'five consecutive numbers are:{lst441}')

lst442=[x44 for x44 in range(num44,num44+5)]
print(f'five consecutive numbers using list comprehenstion:{lst442}')
# # print("------------------------------------------------")
#67 Find all the values in a list are greater than a specified number
lst67=[1,2,3,4,5,5,6,7,8,9,10,1,11,12,14,20,21,23,28,29,30,50,61,99]
num67=int(input('enter a number to get number above from list:'))
lst671=[x67 for x67 in lst67 if x67>num67]
print(lst671)
# # print("------------------------------------------------")
#37 finding common items in two lists
lst371=[1,2,3,4,5,6,7,8,9,10]
lst372=[3,6,9,5,11,14,15,19,20]
lst373=[x37 for x37 in lst372 if x37 in lst371]
print(f'comman elements are:{lst373}')
# # print("------------------------------------------------")
#46 Slect odd items of a list
lst46=[1,2,3,4,5,6,7,8,9,10]
print(f'odd elements in list is:{lst46[0::2]}')
# # print("------------------------------------------------")

#47 Insert an element before each element of a list
lst47=[1,2,3,4,5,6,7,9]
lst471=[]
ele47=input("enter element to append:")
for x47 in lst47:
    lst471.append(ele47)
    lst471.append(x47)
print(lst471)

# # print("------------------------------------------------")
#48 Print a nested lists (each list on a new line) using the print() function
lst48=[[1,2],[3,4],[5,6],[7,8],[9,10]]
print("printing list inside a list line b line")
for x48 in lst48:
    print(x48)
# # print("------------------------------------------------")
#49 Convert list to list of dictionaries
# lst49=[1,2,3,4,5,6,7,8,9]
lst49=['a','b','c','d','e','f']
lst491=[{x49:x49} for x49 in lst49]
print(f'list into dictionary:{lst491}')
# # print("------------------------------------------------")

#56 Convert a string to a list
str56='sachin'
lst56=list(str56)
print(lst56)
# # print("------------------------------------------------")

# 58 Replace the last element in a list with another list

lst58=[1,2,3,4,5,6,7,8,9]
lst581=[3,6,9]
lst58.pop()
lst58.append(lst581)
print(lst58)
# # print("------------------------------------------------")
#61 Create a list of empty dictionaries
num61=int(input('enter the length of list:'))
lst61=[{} for x61 in range(num61)]
print(f'empty dictionariess in list:{lst61}')
# # print("------------------------------------------------")

# #71 Check if all dictionaries in a list are empty or not
# lst71=[{}, {1,2}, {}, {}, {}]
lst71=[{}, {}, {}, {}, {}]
count71=0
for x71 in lst71:
    if len(x71)!=0:
        count71+=1
if count71==0:
    print(f'all dictionaries inside list is empty')
else:
    print(f'not all dictionaries inside list is empty')

# # print("------------------------------------------------")

#73 A list contains group of strings.Convert each word to capital letter and print
lst73=['sachin','virat','dravid','gayle','abd','dhoni']
lst731=[]
for x73 in lst73:
    lst731.append(x73.upper())
print(f'strings in lists converted into upprcase:{lst731}')
# # print("------------------------------------------------")

# 74 Reverse list of elements and print in upper case
lst74=['sachin','virat','dravid','gayle','abd','dhoni']
lst741=[]
for x74 in lst74:
    lst741.append(x74[::-1].upper())
print(f'strings which are reversed in the list :{lst741}')
# # print("------------------------------------------------")

# 75 Write a Python program to convert month name to a number of days
month75=[['jan',31],['feb',28],['mar',31],['apr',30]]
mon75=input("to know num of days in a month,\nenter first three letters of the month: ").lower()
days75=[]
for x75 in month75:
    if mon75==month75[0][0]:
        days75.append(month75[0][1])
print(f'number of days month \"{mon75}\" contains is :{days75[0]} ')

# # print("------------------------------------------------")

# # 25 Select an item randomly
import random
lst25=[1,2,3,4,6,'a','b','c','d']
print(f'random element in a list is:{random.choice(lst25)}')
# # print("------------------------------------------------")

# 29 Get unique values
lst29 = [1,2,3,4,5,6,7,8,9,0,1,5,9,4,3,2,8,0,'a','b','g','u']
lst291=[]
for x29 in lst29:
    if x29 not in lst291:
        lst291.append(x29)
print(f'unique values in a list:{lst291}')

# # print("------------------------------------------------")

#30 Frequency of elements
lst30 = [1,2,3,4,5,6,7,8,9,0,1,5,9,4,3,2,8,0,'a','b','g','u']
lst31=[[x30,lst30.count(x30)] for x30 in lst30 ]
lst301=[]
for x301 in lst31:
    if x301 not in lst301:
        lst301.append(x301)
num30=input('enter element want to know num of times :')

# # print("------------------------------------------------")


