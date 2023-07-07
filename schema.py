from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MyTable1(Base):
    __tablename__ = 'my_table1'
    id = Column(Integer, primary_key=True)

    def __str__(self):
        return f"Table1(id={self.id})"

class MyTable2(Base):
    __tablename__ = 'my_table2'
    id = Column(Integer, primary_key=True)

    def __str__(self):
        return f"Table2(id={self.id})"
