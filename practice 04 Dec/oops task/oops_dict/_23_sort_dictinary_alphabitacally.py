
class Dictalpha:
    def alpha_dict_keys(self,dict1):
        print(f'sorted alphabitically:{sorted(dict1.items(), key=lambda x:x[0])}')


import random
import string

dict1 = dict( (x,0) for x in sorted(string.ascii_lowercase, key=lambda x: random.random()) )
dict2 = dict( (x,x) for x in sorted(string.ascii_lowercase, key=lambda x: random.random()) )
print(dict1)
d1=Dictalpha()
d1.alpha_dict_keys(dict1)

print("--------------------------------------------------------------------------")

class Dictalpha:
    def alpha_dict_keys(self,dict2):
        print(f'sorted alphabitically:{sorted(dict2.items(), key=lambda x:x[1])}')


import random
import string

dict2 = dict( (x,x) for x in sorted(string.ascii_lowercase, key=lambda x: random.random()) )
print(dict2)
d1=Dictalpha()
d1.alpha_dict_keys(dict2)
