class Lists:
    def rem_duplicates_list(self,lst1):
        lst2 = []
        for i in lst1:
            if i not in lst2:
                lst2.append(i)
        print(f'list after removing duplicate ssublist:{lst2}')


lst1=[[1,2],[2,3],[4,5],[2,3],[6,5]]
l1=Lists()
l1.rem_duplicates_list(lst1)
