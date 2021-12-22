from itertools import permutations


'''permutations() returns r-length permutations of elements in the iterable.
It generates all possible permutations in lexicographic order, and there is no repetition of elements.
'''
class Combination_letters:
    def comb_keys(self,val,num):
        # count1=0
        perm=permutations(val,num)
        result = list(perm)
        lst1 = []
        for i11 in result:
            if i11[0] == ')' or i11[-1] == '(':
                result.remove(i11)
            elif i11 not in lst1 and len(i11) == num:
                lst1.append(i11)
        print(lst1)
        print(len(lst1))
        # print("count is:",count1)

num=int(input("enter number of combinations:"))
p='()'
p1='('
p2=')'
op=[i1 for i1 in p1 for j1 in range(0,num)]
cp=[i2 for i2 in p2 for j2 in range(0,num)]
val=[i for i in p for j in range(0,num)]
print(val)
perm = permutations(val, len(val))
d1=Combination_letters()
d1.comb_keys(val,num)



