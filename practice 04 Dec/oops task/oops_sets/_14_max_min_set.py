class Maxmin:
    def __init__(self):
        pass
    def max_min_set(self,set1):
        print(f'maximum number in set is:{sorted(set1,reverse=True)[0]}')
        print(f'minimum number in set is:{sorted(set1, reverse=False)[0]}')

set1 = {1, 5, 7, 9, 3}
s1=Maxmin()
s1.max_min_set(set1)