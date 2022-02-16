"""
Game Rules
Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""

def minion_game(string):
    # your code goes here
    lst=[]
    lst_stuart = []
    lst_kevin = []
    vowels = "aeiou"
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            a=string[i:j]
            lst.append(a)
            if a[0] not in vowels:
                lst_stuart.append(a)
            elif a[0] in vowels:
                lst_kevin.append(a)


    s_score=len(lst_stuart)
    k_score=len(lst_kevin)


    if s_score>k_score:
        print("Stuart",s_score)
    elif s_score<k_score:
        print("Kevin",k_score)

if __name__ == '__main__':
    # s = input()
    s="banana"
    minion_game(s)