from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declatative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String(63), unique=True)
    num = Column(Integer)
    price = Column(Integer)
    category = Column(String(63))
    seller = Column(String(63))

    def __init__(self, name=None, num=None, price=None, cat=None, sell=None):
        self.name = name
        self.num = num
        self.price = price
        self.category = cat
        self.seller = sell

    def __repr__(self):
        return '<Product %r>' % self.name
