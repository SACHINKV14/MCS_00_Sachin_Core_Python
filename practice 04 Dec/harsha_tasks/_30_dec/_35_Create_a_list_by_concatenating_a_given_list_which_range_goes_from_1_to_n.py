class Lists:
    def concatenate_list(self,my_list,n):
        new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
        print(new_list)

my_list = ['p', 'q']
n = 4
l1=Lists()
l1.concatenate_list(my_list,n)