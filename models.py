from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Person(Base):
    __tablename__ = "testAPI"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,unique=True, index=True)
    age = Column(Integer)
    city = Column(String)


