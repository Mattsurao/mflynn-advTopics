from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):

    __tablename__ = 'project'

    id = Column(Integer, primary_key=True)
    # all the following fields will either display by default, or will only
    # display if the user clicks for more details. '(detail)' indicates that
    # it will only be displayed if the user asks for more details
    # the name of the project
    name = Column(String(63), unique=True)
    # my title for the project (detail)
    title = Column(String(31))
    # the genre of the commision. Currently: Classical, Soundtrack
    genre = Column(String(10))
    # a description of the project
    desc = Column(String(383))
    # the person or organization I worked for (detail)
    commisioner = Column(String(63))
    # the time that the project took place (detail)
    date = Column(String(31))
    # text to appear above audio elements of tracks in this project
    audio_text = Column(String(31))

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'title': self.title,
            'genre': self.genre
        }

# an Object to represent a track that a user can listen to
class Track(Base):

    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    # the name of the track
    name = Column(String(127), unique=True)
    # only for projects with multiple tracks
    number = Column(Integer)
    # the name of files associated with this track (in the 'static' folder)
    path = Column(String(31))
    # whether or not the track has audio a user can listen to
    playback = Column(Boolean)
    # whether or not the track has sheet music a user can download
    pdf = Column(Boolean)
    # relationship to the project
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship(Project)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'project': self.project.name
        }
