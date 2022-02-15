from fastapi import FastAPI,Depends
from typing import List
import uvicorn
from scemas import Student,StuBody
from utilities import get_db
from views import add_student_service
# from views import get_all
from database1 import engine
import models
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)


app=FastAPI()

@app.post('/addstudent')# response_model=StuBody)
def add_student(s:Student,db : Session = Depends(get_db)):
    id = s.id
    name = s.name
    s1 = s.s1
    s2 = s.s2
    s3 = s.s3
    s4 = s.s4
    s5 = s.s5
    s6 = s.s6
    status = s.status
    # result = s.result


    return add_student_service(id,name,s1,s2,s3,s4,s5,s6,status,db)#(status,result,db)

# @app.get('/seeall')
# def all1(db:Session = Depends(get_db)):
#     return get_all(db)



if __name__=="__main__":
    uvicorn.run(app,debug=True)
