"""
A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.
"""
def pangrams(s):
    alpha="abcdefghijklmnopqrstuvwxyz"
    s1=s.lower()
    s2=set(s1)
    print(s2)
    for i in alpha:
        if i not in s1:
            a="not pangram"
            break
    else:
        a="pangram"
    return a

    # Write your code here

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)

