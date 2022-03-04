"""
Example

This contains a subsequence of all of the characters in the proper order. Answer YES


This is missing the second 'r'. Answer NO.


There is no 'c' after the first occurrence of an 'a', so answer NO.

"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
import re
def hackerrankInString(s):


    pattern = ".*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*"
    m = re.search(pattern, s)
    if m is not None:
        res="YES"
    else:
        res="NO"
    return res

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)
        print(result)

