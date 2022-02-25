"""
Given the time in numerals we may convert it into words, as shown below:
At , use o' clock. For , use past, and for  use to.
Note the space between the apostrophe and clock in o' clock.
Write a program which prints the time in words for the input given in the format described.
"""

def timeInWords(H, M):
    minutes = ['zero', 'one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine', 'ten',
               'eleven', 'twelve', 'thirteen', 'fourteen',
               'fifteen', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty', 'twenty one', 'twenty two',
               'twenty three', 'twenty four', 'twenty five',
               'twenty six', 'twenty seven', 'twenty eight',
               'twenty nine', 'thirty']
    hours = ['zero', 'one', 'two', 'three', 'four', 'five',
             'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

    if M == 0:
        a=hours[H]+ " o' clock"
    elif M==1:
        a = minutes[M] + " minute past " + hours[H]

    elif M == 15:
        a="quarter past "+ hours[H]
    elif M == 30:
        a="half past "+ hours[H]
    elif M == 45:
        if H == 12:
            a="quarter to "+ hours[1]
        else:
            a="quarter to "+ hours[H + 1]
    elif M > 0 and M < 30:
        a=minutes[M]+ " minutes past "+ hours[H]
    elif M > 30 and M < 60:
        if H == 12:
            a=minutes[60 - M]+ " minutes to "+ hours[1]
        else:
            a=minutes[60 - M]+ " minutes to "+ hours[H + 1]

    return a

if __name__ == '__main__':
    h=1
    m=1

    result = timeInWords(h, m)
    print(result)


