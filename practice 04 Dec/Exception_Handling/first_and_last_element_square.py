'''First,Last elements whose square value is between 1 and 30'''

lst1=['a',2,3,4,5,'b']
# lst1=[1,2,3,4,5,6]
# lst1=[8,2,5,9]
try:
    b=lst1[0]*lst1[0]
    if 1 <= b <=30:
        print(f'square of first number\"{b}\" is in between \'1\' and \'30\'')
    else:
        print(f'square of last number\"{b}\" is not in between \'1\' and \'30\'')
    c=lst1[-1]*lst1[-1]
    if 1 <= c <=30:
        print(f'square of first number\"{c}\" is in between \'1\' and \'30\'')
    else:
        print(f'square of last number\"{c}\" is not in between \'1\' and \'30\'')
except TypeError:
    print('first and last element should be numeric')



