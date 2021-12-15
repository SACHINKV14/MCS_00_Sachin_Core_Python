# function which return reverse of a string

def isPalindrome(s):
    return s == s[::-1]


# Driver code
s = input("enter word:")
ans = isPalindrome(s)

if ans:
    print("word is:",s)
    print("word is palindrome")
else:
    print("word is:", s)
    print("word is not palindrome")