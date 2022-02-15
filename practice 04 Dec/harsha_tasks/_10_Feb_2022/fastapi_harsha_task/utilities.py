
from database1 import SessionLocal
import models,scemas

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def add_student_database(id,name,s1,s2,s3,s4,s5,s6,status,db):
    new_student = models.StudentDetails(id=id,name=name,s1=s1,s2=s2,s3=s3,s4=s4,s5=s5,s6=s6,status=status)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return "data added Successfully"

# def get_all_data(db):
#     new_student=db.query(models.StudentDetails)