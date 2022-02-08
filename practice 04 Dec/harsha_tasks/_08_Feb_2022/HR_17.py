"""Returns
- int: the number of special substrings
Input Format
The first line contains an integer, , the length of .
The second line contains the string .
"""
''' leetcode
5. Longest Palindromic Substring
Medium
Given a string s, return the longest palindromic substring in s'''


def palindromes(text):
    text = text.lower()
    text = text.replace(" ","")
    results = []
    for i in text:
        results.append(i)
    for i in range(len(text)):    #0 to len(str)
            for j in range(0, i):
                txt1 = text[j:i + 1]
                txt1 = text[j:i+1]
                # if txt1 == txt1[::-1] and txt1 not in results:
                if txt1 == txt1[::-1] :
                    results.append(txt1)

    return results

# text = input("enter the string:")
# text="asasd"
# text="abcbaba"
text="aaaa"
res = palindromes(text)
print("res",res,"len",len(res))
