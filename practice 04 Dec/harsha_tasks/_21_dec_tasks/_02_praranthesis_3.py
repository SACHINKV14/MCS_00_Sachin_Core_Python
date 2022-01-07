import balanced_checker
str1='()'
num=int(input("enter the number:"))
str2=[i1 for i1 in str1 for j1 in range(0,num)]
import itertools
string = str2
## itertools.permutations method
permutaion_list = list(itertools.permutations(string))
perm=[]
# print("-------------Permutations In String Format-----------------")
for tup in permutaion_list:
    perm1="".join(tup)
    perm.append(perm1)
lst_perm=[]
for i11 in perm:
    if i11 not in lst_perm and i11[0]=='(' and i11[-1]==')':
        # print(i11)
        lst_perm.append(i11)
# print(len(lst_perm))
lst_bal_par=[]
for i12 in lst_perm:
    if balanced_checker.is_matched(i12):
        lst_bal_par.append(i12)
        # print(string)

print(lst_bal_par)
print(f'number of combinations are:{len(lst_bal_par)}')
