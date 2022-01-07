class Topitems:
    def get_top_items(self,shop):
        print(f'dict sorted using key values:{dict(sorted(shop.items(), key = lambda x: x[1], reverse = True)[:3])}')


shop={'perfume':150,'soap':85,'brush':30,'bag':1000,'pen':10,'chocolate':15}

s1=Topitems()
s1.get_top_items(shop)

print("------------------------------")

print("do it for nested dictionary")
# dict1['shop'][x for x in dict1.values() ]
# for key in dict1:
#     print(key + ':', dict1[key])
# print(dict1['shop'])
# for i,j in dict1.items():
    # print(dict1['shop']['perfume'])
# d1=Topitems()
# d1.dict1(dict1)

# people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
#           2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}
#
# for p_id, p_info in people.items():
#     print("\nPerson ID:", p_id)
#
#     for key in p_info:
#         print(key + ':', p_info[key])