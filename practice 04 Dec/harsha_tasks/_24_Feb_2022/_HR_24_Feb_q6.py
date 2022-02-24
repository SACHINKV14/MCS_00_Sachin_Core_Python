"""
Given two strings, determine if they share a common substring.
A substring may be as small as one character.

"""
def twoStrings(s1, s2):
    for i in s1:
        if i in s2:
            a="YES"
            return a
    else:
        a="NO"
    return a


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)