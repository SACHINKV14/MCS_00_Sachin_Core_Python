class Unikeys:
    def unique_keys(self,dict1):
        dict2={}
        unique_values=set(dict1.values())
        print(unique_values)

dict1={'a':1,'b':2,'c':3,'d':1,'e':3,'g':8}
d1=Unikeys()
d1.unique_keys(dict1)


#doubt need to print all the dict keys and values
