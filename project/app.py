# imports from the Flask framework
from flask import Flask
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
    db.session.add(Track("test", "Soundtrack", "", False))
    db.session.commit()

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
