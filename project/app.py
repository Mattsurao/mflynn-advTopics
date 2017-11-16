from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    

in __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
