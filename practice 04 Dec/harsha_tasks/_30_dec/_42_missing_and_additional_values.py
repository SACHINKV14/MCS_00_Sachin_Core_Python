class Lists:
    def missing_element(self,lst1):
        lst2=lst1.copy()
        lst1.pop()
        # print(lst1)
        # print(lst2)
        missing_list=[x for x in lst2 if x not in lst1]
        print(f'misssing elements in list is:{missing_list}')
    def additional_values(self,lst1):
        lst2 = lst1.copy()
        for i in [9,8,7]:
            lst1.append(i)
        additional_list = [x for x in lst1 if x not in lst2]
        print(f'additional elements in list is:{additional_list}')


lst1=[1,2,3,4]
l1=Lists()
l1.missing_element(lst1)
l1.additional_values(lst1)