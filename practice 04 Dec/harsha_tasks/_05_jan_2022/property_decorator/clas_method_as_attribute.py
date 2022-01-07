# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#
#     @property
#     def msg(self):
#         return self.name +" got grade "+self.grade
#
# stud1 = Student("sachin","A")
# stud1.grade="A"
# print("name",stud1.name)
# print("grade",stud1.grade)
# print(stud1.msg)  #allowuis to use method as attribute


print("------------------")
#setter method

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property
    def msg(self):
        return self.name +" got grade "+self.grade


    def setter(self,msg):
        sent=msg.split(" ")
        self.name=sent[0]
        self.grade=sent[-1]

stud1 = Student("sachin","A")
stud1.setter("dhoni got grade A") 
print("name",stud1.name)
print("grade",stud1.grade)
print(stud1.msg)  #allowuis to use method as attribute

print("-------------------")
#setter method

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    @property
    def msg(self):
        return self.name +" got grade "+self.grade

    @msg.setter
    def msg(self,msg):
        sent=msg.split(" ")
        self.name=sent[0]
        self.grade=sent[-1]

stud1 = Student("sachin","A")
# stud1.setter("dhoni got grade A")
stud1.msg="dhoni got grade A"
print("name",stud1.name)
print("grade",stud1.grade)
print(stud1.msg)  #allowuis to use method as attribute
