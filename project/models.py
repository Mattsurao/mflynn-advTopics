from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):

    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    # the name of the project
    name = Column(String(63), unique=True)
    # my title for the project
    title = Column(String(31))
    # the person or organization I worked for
    commisioner = Column(String(63))
    # the genre of the commision. Currently: Classical, Soundtrack
    genre = Column(String(10))

# an Object to represent a track that a user can listen to
class Track(Base):

    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    # the name of the track
    name = Column(String(127), unique=True)
    # the path to the file
    path = Column(String(255))
    # 0 = the whole track plays.  1 = a 30 second sample.  2 = no playback
    full = Column(Integer)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)
