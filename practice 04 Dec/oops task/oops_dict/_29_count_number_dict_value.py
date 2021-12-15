#29 Count number of items in a dictionary value that is a list

class Countdictvalue:
    def count_dict_list_value(self,dict1):
        for k, v in dict1.items():
            if type(v) == list:
                print(f'for key {k}, len of value is:{len(v)}')



dict1={'a':[1,3,2,1,5,6,7,9],'b':'a','c':True,'d':[9,8,7,6]}
a1=Countdictvalue()
a1.count_dict_list_value(dict1)
