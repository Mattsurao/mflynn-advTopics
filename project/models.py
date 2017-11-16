from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# an Object to represent a track that a user can listen to
class Track(Base):

    __tablename__ = 'tracks'

    id = Column(Integer, primary_key=True)
    # the name of the track
    name = Column(String(127), unique=True)
    # acceptable values: Classical, Soundtrack
    genre = Column(String(10))
    # the path to the file
    path = Column(String(255))
    # indicates if the whole track will play or if just a 30 second sample will
    full = Column(Boolean)

    def __init__(self, name=None, genre="Soundtrack", path=None, full=False):
        self.name = name
        self.genre = genre
        self.path = path
        self.full = full
