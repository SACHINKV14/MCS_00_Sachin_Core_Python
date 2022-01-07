'''242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''

word='sachin'
print(f'word is :{word}')
word=word.lower()
user_word=input('enter word:')
# user_word='ahinsc'
user_word=user_word.lower()
ws="".join(sorted(word))
uws="".join(sorted(user_word))
print(ws,'\t',uws)

if (len(ws)==len(uws)) and ws==uws:
    print(f'\"{user_word}\" is anagram of \"{word}\"')
else:
    print(f'\"{user_word}\" is not anagram of \"{word}\"')




