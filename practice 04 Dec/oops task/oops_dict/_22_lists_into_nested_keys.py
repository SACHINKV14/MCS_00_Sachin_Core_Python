class Dictnestedkey:
    def nested_dict(self,lst1,lst2):
        D = dict(zip(lst1,lst2))
        print(f'nested dict using 2 lists is:{D}')

lst1 = ['stu1','stu2','stu3']

lst2 = [{'name': 'sa', 'marks': 85},
        {'name': 'ch', 'marks': 75},
        {'name': 'in', 'marks': 80}]

d1=Dictnestedkey()
d1.nested_dict(lst1,lst2)