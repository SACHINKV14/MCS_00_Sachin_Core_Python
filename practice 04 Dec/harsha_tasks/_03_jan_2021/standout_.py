'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
'''Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Vparathrsis():
    def valid_paranthesis(self,str1):
        # if len(str1)==2:
        #     if (str1[0]=='(' and str1[0+1]==')') or (str1[0]=='[' and str1[0+1]==']') or (str1[0]=='{' and str1[0+1]=='}'):
        #         print('True')
        #     elif (str1[0]=='(' and str1[0+1]!=')') or (str1[0]=='[' and str1[0+1]!=']') or (str1[0]=='{' and str1[0+1]!='}'):
        #         print('False')
        if len(str1)>=2:
            for i in str1[0::2]:
                b=str1.index(i)
                if (str1[b]=='(' and str1[b+1]==')') or (str1[b]=='[' and str1[b+1]==']') or (str1[b]=='{' and str1[b+1]=='}'):
                    pass
                else:
                    print('false')
                    break
            else:
                print(True)


s = "()"
v1=Vparathrsis()
v1.valid_paranthesis(s)