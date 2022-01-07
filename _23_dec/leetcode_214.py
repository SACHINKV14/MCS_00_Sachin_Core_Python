def palindromes(text):
    text = text.lower()
    text = text.replace(" ","")
    results = []
    for i in range(len(text)):    #0 to len(str)
        for j in range(0, i):
            txt1 = text[j:i + 1]
            if txt1 == txt1[::-1] and txt1 not in results:
                results.append(txt1)
    return results


text = input("enter the string:")
if text!=text[::-1]:
    print(f'palindrome of a entered string is {text[-1:0:-1] +text}')
res = palindromes(text)
# if text==res:
#     print(f'entered string \"{text}\" is a palindrome')
# elif str1.index(res) == 0:
#     print(f'{str1[len(res)]}')
#     print(f'palindrome of a entered string is:{str1[len(res)] + str1}')
# else:
#     str2 = str1[-1:0:-1] + str1
#     print(f'original string:\"{str1}\"\n'
#           f'string converted to palindrome:\"{str2}\"')
