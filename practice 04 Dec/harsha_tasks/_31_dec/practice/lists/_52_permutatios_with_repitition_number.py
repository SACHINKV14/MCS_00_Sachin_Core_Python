import itertools
class Permutations:
    def print_permutations(self,str1):
        permutaion_list = list(itertools.permutations(str1))
        lst1 = []
        for i in permutaion_list:
            b = "".join(i)
            lst1.append(b)
        print(f'number of permutations possible are:{len(lst1)}')
        print(lst1)

str1="aacd"
l1=Permutations()
l1.print_permutations(str1)
