
"""A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

"""

if __name__ == '__main__':
    s = "qA2"
    for i in s:
        if i.isalnum():
            print(True)
            break
    else:
        print(False)

    for i in s:
        if i.isalpha():
            print(True)
            break
    else:
        print(False)

    for i in s:
        if i.isdigit():
            print(True)
            break
    else:
        print(False)

    for i in s:
        if i.islower():
            print(True)
            break
    else:
        print(False)

    for i in s:
        if i.isupper():
            print(True)
            break
    else:
        print(False)