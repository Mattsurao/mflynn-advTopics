# imports from the Flask framework
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# imports for database handling
from models import Base, Track

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    # set up the database
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Track("Random Encounter", "Soundtrack",
            "Random Encounter 2.mp3", True))
    db.session.add(Track("Human Towns", "Soundtrack", "Human Towns.mp3", True))
    db.session.add(Track("Mystery", "Soundtrack", "Mystery.mp3", True))
    db.session.commit()

@app.route('/music')
def music():
    track_list = db.session.query(Track).all()
    return render_template('music.html', tracks=track_list)

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
