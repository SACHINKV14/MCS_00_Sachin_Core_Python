'''
Apply hike based on rating on a scale of 5.
If rating is 4 to 5 - 30%
             3 to 4 - 20%
             2 to 3 - 10%
             <2     -  no hike
'''

# class
class Employee:
    # local variables   - eid, name, sal
    # instance variables - self.eid self.name self.sal - instance variables

    def __init__(self, eid, name, sal):
        print("Self address : ",self)
        self.eid = eid
        self.name = name
        self.sal = sal

    # instance methods
    def get_edata(self):
        print("Employee information : ",self.eid, self.name, self.sal)

    def apply_hike(self, rating):
        print("Employee hike with rating : ", rating)
        if rating >= 4 and rating <= 5:
            hike = self.sal*30/100
            print(" Hike is :: ", hike)
        elif rating >= 3 and rating < 4:
            hike = self.sal*20/100
            print(" Hike is :: ", hike)
        elif rating >= 2 and rating < 3:
            hike = self.sal*10/100
            print(" Hike is :: ", hike)
        else:
            print(" Hike is :: ", 0)

#
# #    # to take only list names
# # lst=['madhu','ranjithac']
# #
# # for i in lst:
# #     rajitha = Employee(101, i, 20000)
# #     rajitha.get_edata()
# #     val = int(input("Please enter rating: "))
# #     rajitha.apply_hike(val)  # Employee.apply_hike(rajitha, val)
# #
#
#
# #to take names and salaries
# dict={'madhu':15000,'ranjitha':20000}
# for i in dict:
#     p = Employee(101, i, dict[i])
#     p.get_edata()
#     val = int(input("Please enter rating: "))
#     p.apply_hike(val)  # Employee.apply_hike(rajitha, val)
#


ndict={100:{'madhu':15000},
       101:{'ranjitha':20000}}
for ndict_id, ndict_info in ndict.items():
    # print("\nPerson ID:", ndict_id)

    for key in ndict_info:
        # print(key + ':', ndict_info[key])
        p = Employee(ndict_id, key, ndict_info[key])
        p.get_edata()
        val = int(input("Please enter rating: "))
        p.apply_hike(val)  # Employee.apply_hike(rajitha, val)