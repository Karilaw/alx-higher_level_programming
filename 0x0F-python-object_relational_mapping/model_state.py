#!/usr/bin/python3
"""a python script that cointains class
defination"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class definition"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    """Main method that creates the State table in the database"""
    engine = create_engine(
            'mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa',
            pool_pre_ping=True
            )
    Base.metadata.create_all(engine)
