import string
#morse codes
lst1=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#create lowercase alphabets list
lst2 = list(string.ascii_lowercase)
# print(lst2)

#crete dict alphbets as key,moorse codes as values
dict1={x:y for x,y in zip(lst2,lst1)}
# print(dict1)

#user input
str1=input("enter string :").lower()
str1 = str1.replace(" ","")
lst_str1=list(str1)

lst_moorse=[]
for i in str1:
    if i in dict1.keys():
        lst_moorse.append(dict1[i])
# print(lst_moorse)
for j in lst_moorse:
    str_moorse="".join(lst_moorse)

print(f'string is :\t{str1}\nmoorse code of string is: {str_moorse}')


