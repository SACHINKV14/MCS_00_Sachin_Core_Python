from database import SessionLocal
import models,schemas

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


def add_student_utilities(id,name,marks1,marks2,marks3,marks4,marks5,marks6,avg,status,chance,db):
    new_student=models.StudentDetails(id=id,name=name,marks1=marks1,marks2=marks2,
                                      marks3=marks3,marks4=marks4,marks5=marks5,marks6=marks6,
                                      avg=avg,status=status,chance=chance)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return "Student data added Successfully"
