'''from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Entry(Base):
    __tablename__ = 'tbl_weight'

    name = Column(String(45), primary_key=True)
    date = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)

engine = create_engine('mysql+mysqldb://root:password@localhost:3306/wetr')

Base.metadata.create_all(engine)
'''

from app import db

class Post(db.Model):
    __tablename__ = 'tbl_weight'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True)
    date = db.Column(db.String(30), nullable=True)
    weight = db.Column(db.Float, nullable=True)

    def __init__(self, name, date, weight):
        self.name = name
        self.date = date
        self.weight = weight

    def __repr__(self):
        return '{0};{1};{2}'.format(self.name, self.date, self.weight)
