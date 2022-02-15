from unicodedata import name
from pydantic import BaseModel

class Student(BaseModel):
    id:int
    name:str
    s1:int
    s2:int
    s3:int
    s4:int
    s5:int
    s6:int
    # s4: int=None
    # s5: int=None
    # s6: int=None
    status:str
    # result:float


class StuBody(BaseModel):
    id=int
    name:str
    status:str
    result:float
    class Config:
        orm_mode=True
