class Sortkey:
    def sort_key(self,dict1):
        print(f'dict sorted using key values:{dict(sorted(dict1.items(), key = lambda x: x[0], reverse = False))}')

dict1={'e':4,'b':5,'c':7,'d':3,'f':8,'g':1,'a':2,}
d1=Sortkey()
d1.sort_key(dict1)
