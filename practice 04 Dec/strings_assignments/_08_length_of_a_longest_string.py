# colors=['green','blue','yellow']
# max_len=-1
# for word in colors:
#     print(word,'length is:',len(word))
#     if len(word)>max_len:
#         max_len=len(word)
#         res=word
#         # print(res)
# print(res)


# #using built in function max() using key as keyword
# colors1=['green','blue','yellow']
# long_word=max(colors1,key=len)
# short_word=min(colors1,key=len)
# print(long_word)
# print(short_word)

txt1=input("Enter text here:")
max_len=-1
for word in txt1.split():
    # print(word,'length is:',len(word))
    if len(word)>max_len:
        max_len=len(word)

        res=word
        # print(f'{word} length is {max_len}')
print(f'{word} length is {max_len}')
# print(res)