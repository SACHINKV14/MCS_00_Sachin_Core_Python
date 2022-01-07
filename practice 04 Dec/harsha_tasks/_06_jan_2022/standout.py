'''
12. Integer to Roman
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
def printRoman(number):
    dict1={1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    roman_number=""
    lst=[]
    for k,v in dict1.items():
        div = number // k      #gives remainder
        r_number=v*div         #multiplying its roman number into
        lst.append(r_number)
        number=number-(k*div)

    roman_number="".join(lst)
    print(roman_number)


your_number=int(input('enter number:'))
printRoman(your_number)

'''Initially number = 3549, Since 3549 >= 1000 ; largest base value will be 1000 initially. 
And Divide 3549/1000. Quotient = 3, Remainder =549. The corresponding symbol M will be repeated thrice.
Now, number become 549 and 1000 > 549 >= 500, largest base value will be 500 then divide 549/500. 
Quotient = 1, Remainder =49. The corresponding symbol D will be repeated once.
Now, number = 49 and 50 > 49 >= 40, largest base value is 40. Then divide 49/40. 
Quotient = 1, Remainder = 9. The corresponding symbol XL will be repeated once.
Now, number = 9 and 10> 9 >= 9, largest base value is 9. Then divide 9/9. 
Quotient = 1, Remainder = 0. The corresponding symbol IX will be repeated once.
Finally, the number becomes 0, the algorithm stops here. The output obtained MMMDXLIX.'''





