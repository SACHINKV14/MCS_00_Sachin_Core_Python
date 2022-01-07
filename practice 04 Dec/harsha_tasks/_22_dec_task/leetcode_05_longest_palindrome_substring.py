''' leetcode
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s'''


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
res = palindromes(text)

longest_palindrome = [x for x in sorted(res, key=len, reverse=True)]
if len(longest_palindrome)==0:
    print('\"no palindrome substring\"')
else:
    print(f'palindromic substrings are:{res}')
    print(f'number of palindrome substrings are:{len(longest_palindrome)}')
    print(f'first longest palindrome substring in given string is:{longest_palindrome[0]}')
