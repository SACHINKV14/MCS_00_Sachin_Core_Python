'''__init__ with inheritance
Inheritance is the capability of one class to derive or inherit the properties from some other class.
Let’s consider the below example to see how __init__ works in inheritance.'''




# Python program to
# demonstrate init with
# inheritance

class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)    #to call init of class A
        print("B init called")
        self.something = something


obj = B("Something")


'''So, the parent class constructor is called first. But in Python,
 it is not compulsory that parent class constructor will always be called first. 
 The order in which the __init__ method is called for a parent or a child class can be modified. 
This can simply be done by calling the parent class constructor after the body of child class constructor.'''


# Python program to
# demonstrate init with
# inheritance

class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something


class B(A):
    def __init__(self, something):
        print("B init called")
        self.something = something
        # Calling init of parent class
        A.__init__(self, something)


obj = B("Something")