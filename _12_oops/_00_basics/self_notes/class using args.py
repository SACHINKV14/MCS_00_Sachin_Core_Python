from MyClass import MyClass


class Person:
    def __init__(self, name, age):
        print('init called')
        self.name = name
        self.age = age

    def display(self):
        print('in display')
        print("Name-", self.name)
        print("Age-", self.age)
        # object of class MyClass
        obj = MyClass()
        # passing person object to
        # method of MyClass (self = person here)
        obj.my_method(self)


person = Person('John', 40)
person.display()er1=doWorkWithItems(divX,divY,divZ,....)