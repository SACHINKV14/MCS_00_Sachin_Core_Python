class Asendingdesending:
    def __init__(self):
        pass
    def asd_des(self,dict1):
        print(f'Asending values of dict values:{sorted(dict1.values())}')
        print(f'Desending values of dict values:{sorted(dict1.values(), reverse = True)}')

dict1={'a':2,'b':5,'c':7,'d':3,'e':4,'f':8,'g':1}
d1=Asendingdesending()
d1.asd_des(dict1)

print("---------------------------------------------------")



'''Use dict.items() to get a list of tuple pairs from d and sort it using a lambda function and sorted().
Use dict() to convert the sorted list back to a dictionary.
Use the reverse parameter in sorted() to sort the dictionary in reverse order, based on the second argument.
'''



class Asendingdesending:
    def __init__(self):
        pass
    def asd_des(self,dict1):
        print(f'Asending values of dict values:{dict(sorted(dict1.items(), key = lambda x: x[1], reverse = False))}')
        print(f'Desending values of dict values:{dict(sorted(dict1.items(), key = lambda x: x[1], reverse = True))}')
sorted
dict1={'a':2,'b':5,'c':7,'d':3,'e':4,'f':8,'g':1}
d1=Asendingdesending()
d1.asd_des(dict1)