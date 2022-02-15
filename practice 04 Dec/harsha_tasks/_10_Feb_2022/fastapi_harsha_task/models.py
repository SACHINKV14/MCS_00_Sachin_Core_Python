from sqlalchemy import Column,String,Integer,Float
from database1 import Base, engine

class StudentDetails(Base):
    __tablename__='mcs'
    id=Column(Integer,primary_key=True)
    name=Column(String(255),index=True)
    phone=Column(Integer)
    s1=Column(Integer)
    s2=Column(Integer)
    s3=Column(Integer)
    s4=Column(Integer)
    s5=Column(Integer)
    s6=Column(Integer)
    status=Column(String(30), index=True)
    result=Column(Float)



# Base.metadata.create_all(bind=engine)