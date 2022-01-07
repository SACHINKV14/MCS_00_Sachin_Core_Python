def longestPalindrome(s) -> str:
    # Create a string to store our resultant palindrome
    palindrome = ''
    # loop through the input string
    for i in range(len(s)):
        # print(i)
        # loop backwards through the input string
        for j in range(len(s), i, -1):
            print(j)
            # Break if out of range
            if len(palindrome) >= j-i:
                break
            # Update variable if matches
            elif s[i:j] == s[i:j][::-1]:
                # print(s[i:j])
                palindrome = s[i:j]
                break
    return palindrome

s='alayalam'
s1=longestPalindrome(s)
