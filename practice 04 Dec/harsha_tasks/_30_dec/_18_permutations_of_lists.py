import itertools
class Permutations:
    def print_permutations(self,list1):
        str1 = "".join(list1)
        permutaion_list = list(itertools.permutations(list1))
        lst1 = []
        for i in permutaion_list:
            b = "".join(i)
            lst1.append(b)
        print(f'number of permutations possible are:{len(lst1)}')
        print(lst1)

list1=['a','e','c','d']
l1=Permutations()
l1.print_permutations(list1)
