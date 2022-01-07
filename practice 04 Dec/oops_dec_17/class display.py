

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

        # passing person object to
        # method of MyClass (self = person here)



person = Person('John', 40)
person.display()              #displays everything in the block