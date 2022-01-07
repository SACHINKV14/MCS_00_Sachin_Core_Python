class Dictkeyremove:
    def dict_duplicate_remove(self,test_dict):
        # Remove duplicate values in dictionary
        # Using loop
        temp = []
        res = dict()
        for key, val in test_dict.items():
            if val not in temp:
                temp.append(val)
                res[key] = val
        print(res)

test_dict = {'sac': 10, 'is': 15, 'in': 20, 'good': 10, 'cool': 20}
d1=Dictkeyremove()
d1.dict_duplicate_remove(test_dict)








