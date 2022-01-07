def remove(string):
    # Base Case
    if not string:
        return ""

    # Recursive Case
    if string[0] == "\t" or string[0] == " ":
        return remove(string[1:])
    else:
        return string[0] + remove(string[1:])
# Driver Code
print(remove("india is my  country"))