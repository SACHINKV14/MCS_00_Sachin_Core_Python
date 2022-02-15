from utilities import add_student_database
# from utilities import get_all_data

def add_student_service(id,name,s1,s2,s3,s4,s5,s6,db):
    marks = 0
    # if s4:
    #     marks = (s1 + s2 + s3 + s4) / 4
    #     if s5:
    #         marks = (s1 + s2 + s3 + s4 + s5) / 5
    #         if s6:
    marks = (s1 + s2 + s3 + s4 + s5 + s6) / 6
    # else:
    #     marks = (sub1 + sub2 + sub3) / 3
    result = marks
    status = 'fail'
    if marks >= 90:
        # chance = False
        status = 'distinction'
    elif marks >= 75 and marks <= 90:
        # chance = False
        status = 'average'
    elif marks <= 75:
        # chance = True
        status = "fail"
    return add_student_database(id=id, name=name, s1=s1, s2=s2, s3=s3, s4=s4, s5=s5, s6=s6,
                                     status=status,result=marks,db=db)


# def get_all(db):
#     return get_all_data(db)

# def alter(id,name,db):
#     return update(id,name,db)