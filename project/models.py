from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative_base import declarative_base

Base = declarative_base()

class Tracks(Base):

    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    name = Column(String(127))
