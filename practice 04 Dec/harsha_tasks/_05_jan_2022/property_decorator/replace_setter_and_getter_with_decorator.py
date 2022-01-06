class Student:
    def __init__(self,marks):
        self.__marks=marks   #making private variable
    def per(self):
        return (self.__marks/600)*100
    def setter(self,value):  #new value should pass here
        self.__marks=value
    def getter(self):
        return self.__marks


#client code
s=Student(400)

#change mark value
# s.marks=500
#to set value
s.setter(500)

#print(s.marks)
print(s.getter())
# print(s.marks)
print(s.per(),"%")

print("------------------------")
class Student:
    def __init__(self,marks):
        self.__marks=marks   #making private variable
    def per(self):
        return (self.__marks/600)*100

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):  #new value should pass here
        self.__marks=value




#client code
#we are not calling setterand getter method
s=Student(400)
#change mark value
s.marks=500
print(s.marks)
print(s.per(),"%")


print("---------------------------")
#set limit to the value
class Student:
    def __init__(self,marks):
        self.__marks=marks   #making private variable
    def per(self):
        return (self.__marks/600)*100

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self,value):  #new value should pass here
        if value<0 or value>600:
            print("can't set value stick to previous value!!!")
        else:
            print("Setting value:",value)
            self.__marks=value


#client code
#we are not calling setterand getter method
s=Student(400)
#change mark value
s.marks=601
print(s.marks)
print(s.per(),"%")

print("------------------------")
# another way
class Student:
    def __init__(self,marks):
        self.__marks=marks   #making private variable
    def per(self):
        return (self.__marks/600)*100


    def getter(self):
        print("getting value:",end=" ")
        return self.__marks

    def setter(self,value):  #new value should pass here
        if value<0 or value>600:
            print("can't set value stick to previous value!!!")
        else:
            print("Setting value:",value)
            self.__marks=value

    marks = property(getter,setter)

#client code
#we are not calling setterand getter method
s=Student(400)
#change mark value
s.marks=300
print(s.marks)
print(s.per(),"%")
