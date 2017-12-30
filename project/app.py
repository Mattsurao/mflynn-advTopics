# imports from the Flask framework
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# imports for database handling
from models import Base, Track, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False

@app.before_first_request
def setup():
    # set up the database
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    # get the project descriptions from the text file
    f = open('static\descriptions.txt', 'r')
    descriptions = f.readlines()
    f.close()
    # project1 - No Hero
    d = get_description(descriptions, 0)
    project1 = Project(name='No Hero',title='Audio Director',genre='Soundtrack',
                       audio_text='Audio from the game:', desc=d,
                       date='2016 - Ongoing')
    db.session.add(project1)
    db.session.add(Track(name='Mystery', path='Mystery', number=1, pdf=True,
                         playback=True, runtime="2:00", project=project1))
    db.session.add(Track(name='Town 1', path='Human Towns', number=2, pdf=False,
                         playback=True, runtime='1:52', project=project1))
    db.session.add(Track(name='Battle',path='Random Encounter 2',playback=True,
                         number=3, runtime='2:16', pdf=False, project=project1))
    # project2 - Quintet of Night and Day
    d = get_description(descriptions, 1)
    project2 = Project(name='Quintet of Night and Day', title='Composer',
                       commisioner=None, genre='Classical', desc=d,
                       date='Dec. 2016 - Jan. 2017')
    db.session.add(project2)
    db.session.add(Track(name='Quintet of Night and Day', path='Quintet',
                         playback=False, pdf=True, runtime='12:39',
                         project=project2))
    # project2 - The Top
    d = get_description(descriptions, 2)
    project3 = Project(name='The Top', title='Composer', genre='Classical',
                       commisioner=None, desc=d, date='Apr. - May 2017')
    db.session.add(project3)
    db.session.add(Track(name='The Top', path='The Top', playback=False,
                         pdf=True, runtime='7:22', project=project3))
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

def get_description(descriptions, index):
    if len(descriptions) > index:
        return descriptions[index]
    else:
        return None

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
