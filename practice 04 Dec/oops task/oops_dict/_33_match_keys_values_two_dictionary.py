class Matchdict:
    def match_two_dict(self,dict1,dict2):
        count1=0
        for item in dict1.items():
            if item in dict2.items():
                count1 += 1
        print(f'found \"{count1}\" total number of matched items in two dict: ')
dict1={'a':1,'b':2,'c':3}
dict2={'a':4,'b':2,'d':3}
d1=Matchdict()
d1.match_two_dict(dict1,dict2)
