class Dictcount:
    def count_len_value(self,dict1):
        for k, v in dict1.items():
            print(f'for dict key \'{k}\' length of value is\"{len(v)}\"')

dict1={'a':[1,2,3,4],'b':(True,False),'c':'sachin','d':{1,5,3,9,'sachin','cool'}}
d1=Dictcount()
d1.count_len_value(dict1)