from itertools import permutations


'''permutations() returns r-length permutations of elements in the iterable.
It generates all possible permutations in lexicographic order, and there is no repetition of elements.
'''
class Combination_letters:
    def comb_keys(self,dict1):
        lst1 = []
        for key in dict1.keys():
            lst1.append(key)
        count1=0
        for i in permutations(lst1,4):
            count1 +=1
            print(i)
        print("count is:",count1)

dict1={'a':1,'b':2,'c':3,'d':4}
d1=Combination_letters()
d1.comb_keys(dict1)



