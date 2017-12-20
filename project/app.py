# imports from the Flask framework
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# imports for database handling
from models import Base, Track, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    # set up the database
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    # project1 - No Hero
    project1 = Project(name='No Hero', title='Audio Director',
                       commisioner='Myself', genre='Soundtrack')
    db.session.add(project1)
    db.session.add(Track(name='Mystery', path='Mystery', playback=True,
                         pdf=True, project=project1))
    db.session.add(Track(name='Town 1', path='Human Towns', playback=True,
                         pdf=False, project=project1))
    db.session.add(Track(name='Battle', path='Random Encounter', playback=True,
                         pdf=False, project=project1))
    # project2 - Quintet of Night and Day
    project2 = Project(name='Quintet of Night and Day', title='Composer',
                       commisioner='Settlement Music School', genre='Classical')
    db.session.add(project2)
    db.session.add(Track(name='Quintet of Night and Day', path='Quintet',
                         playback=False, pdf=True, project=project2))
    # project2 - The Top
    project3 = Project(name='The Top', title='Composer', genre='Classical',
                       commisioner='Settlement Music School')
    db.session.add(project3)
    db.session.add(Track(name='The Top', path='The Top', playback=False,
                         pdf=True, project=project3))
    db.session.commit()

@app.route('/music')
def music():
    projects = db.session.query(Project).all()
    tracks = db.session.query(Track).all()
    # sort the tracks by project, and put the in a 2D list
    sort = []
    for i in projects:
        sort.append([])
    for track in tracks:
        sort[track.project_id - 1].append(track)
    return render_template('music.html', projects=projects, all_tracks=sort)

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
