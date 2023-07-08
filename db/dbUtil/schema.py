from sqlalchemy import *
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dummy(Base):
    __tablename__ = 'dummy_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)
