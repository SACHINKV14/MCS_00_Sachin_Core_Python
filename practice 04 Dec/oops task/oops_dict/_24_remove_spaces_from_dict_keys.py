#Remove spaces from dictionary keys.
class Keyspaceremove:
    def dict_key_space_remove(self,dict1):
        print(f'original dictionary is:{dict1} ')
        lst1 = []
        lst2 = dict1.values()
        for i in dict1.keys():
            i = i.replace(' ', '')
            lst1.append(i)
        # print(lst1)
        dict2 = {x: y for (x, y) in zip(lst1, lst2)}
        print(f'dictionary keys after removing spaces in keys{dict2}')


dict1={" a":1,"b ":2," c ":3,'d  ':4}
a1=Keyspaceremove()
a1.dict_key_space_remove(dict1)


