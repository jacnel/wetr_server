from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Entry(Base):
    __tablename__ = 'tbl_weight'

    name = Column(String(45), primary_key=True)
    date = Column(Integer(12), nullable=True)
    weight = Column(Float, nullable=True)

engine = create_engine('mysql://root:password@ec2-35-167-186-207.us-west-2.compute.amazonaws.com:3306/wetr')

Base.metadata.create_all()
