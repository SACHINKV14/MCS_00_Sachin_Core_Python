class Student:
    def __init__(self,student_id,student_name,roll_num):
        self.student_id = student_id
        self.student_name = student_name
        self.roll_num = roll_num

    def print_details(self):
        print(f'student name:{self.student_name}\nstudent id is:{self.student_id}\nstudent roll numer is:{self.roll_num}')

name=input("enter your name:")
id=int(input("enter your id number:")
r_num=int(input("enter roll number:"))
