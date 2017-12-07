# imports from the Flask framework
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# imports for database handling
from models import Base, Track, Project

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    # set up the database
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    project1 = db.session.add(Project(name='No Hero', title='Audio Director',
                                      commisioner='Myself', genre='Soundtrack'))
    db.session.add(Track(name='Mystery', path='Mystery.mp3', full=0,
                         project=project1))
    db.session.add(Track(name='Town 1', path='Human Towns.mp3', full=0,
                         project=project1))
    db.session.add(Track(name='Battle', path='Random Encounter.mp3', full=0,
                         project=project1))
    db.session.commit()

@app.route('/music')
def music():
    projects = db.session.query(Project).all()
    tracks = db.session.query(Track).all()
    return render_template('music.html', projects=projects, tracks=tracks)

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
