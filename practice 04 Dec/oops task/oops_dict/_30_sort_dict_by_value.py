class Sortdict:
    def sort_dict(self,dict1):
        dict2={k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
        print(f'dictionary after sorting by value\n{dict2}')

#can be used for sorting students with their marks card
dict1={'a': 2, 'b': 4, 'c': 3, 'd': 1, 'e': 0}
d1=Sortdict()
d1.sort_dict(dict1)