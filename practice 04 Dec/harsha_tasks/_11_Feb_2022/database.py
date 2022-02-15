from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from database import engine


SQLALCHEMY_DATABASE_URL ="mysql://sachin:sachin123@127.0.0.1:3306/schoolstudent"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

