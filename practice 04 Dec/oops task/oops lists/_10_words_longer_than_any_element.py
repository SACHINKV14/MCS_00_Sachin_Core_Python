class Lists:
    def longer_word(self,lst1):
        lst2=[x for x in sorted(lst1,key=len,reverse=True )]
        print(f'longer element in list is:{lst2[0]}')

lst1=['sa','nhvchvkhbk','s','liju','a']
l1=Lists()
l1.longer_word(lst1)
