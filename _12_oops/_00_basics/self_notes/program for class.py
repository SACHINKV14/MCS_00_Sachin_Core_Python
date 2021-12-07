# #program to create a class
# class sachin :
#     varabl = 'Hello'
#
# def function(self) :
#     print ("This is a message Hello")
#
# class Sachin(object) :
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# def sample(self) :
#     print ("This is just a sample code")

#Creating objects of class(Instance of a class)

class student:
    def __init__(self, roll, name):
        self.r = roll
        self.n = name
        print((self.r,self.n))


# # ...
# stud1 = student(1, "Alex")       #objects
# stud2 = student(2, "Karlos")
#
# print("Data successfully stored in variables")
#


class Dog():
    def __init__(self, name):
        self.name = name  # self.name is now an attribute of the Dog class and has a specific value for each instance

    def speak(self):
        pass

tim = Dog("Tim")