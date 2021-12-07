
#process of inheriting the properties of the parent class into a child class is called inheritance.
#base class
class A:
    dic={'A': {'id': '100', 'name': 'he', 'salary': {'1': 10, 'hra': 10,'sa':100}}}
    # 1. STATE
    def __init__(self):
        pass

    def print_evenid_salary(eid, ename, esal):
        print("Employee details are ", eid, ename, esal)


#child class
class B(A):
    def __init__(self):
        pass
    def B_info(self):
        print('Inside B class')

# Create object of B
b = B()


