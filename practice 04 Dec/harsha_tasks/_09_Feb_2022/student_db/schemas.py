from pydantic import BaseModel
class Student(BaseModel):
    sname : str
    sid : int
    sloc : str
    sclass : int