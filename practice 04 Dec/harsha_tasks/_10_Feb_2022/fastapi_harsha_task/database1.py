from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@127.0.0.1:5432/abhi"

SQLALCHEMY_DATABASE_URL ="mysql://root:Kalkunte@369@127.0.0.1:3306/school"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

