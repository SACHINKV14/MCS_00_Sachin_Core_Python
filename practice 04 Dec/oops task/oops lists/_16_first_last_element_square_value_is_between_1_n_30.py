class Lists:
    def square_num(self,lst1):
        lst2=[x for x in sorted(lst1,reverse=False) if x*x>=1 and x*x<=30 ]
        print(f'first element square is between 1 and 30 :{lst2[0]}\n'
              f'last element square is between 1 and 30 :{lst2[-1]}')

lst1=[1,6,4,5,6,7,9,2,4,5,]
l1=Lists()
l1.square_num(lst1)
