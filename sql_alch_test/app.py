from flask import Flask
from models import Base, Product
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

@app.before_first_request
def setup():
    Base.metadata.drop_all(bind=db.engine)
    Base.metadata.create_all(bind=db.engine)
    db.session.add(Product("Fork", 83, 295, "Culinary", "Brandon's Forks"))
    db.session.add(Product("Spoon", 459, 349, "Culinary",
        "Frederic's Food Forum"))
    db.session.add(Product("Spork", 17, 595, "Culinary",
        "Frederic's Food Forum"))
    db.session.add(Product("Butter", 89, 895, "Culinary",
        "Frederic's Food Forum"))
    db.session.add(Product("Cookie", 67, 195, "Culinary","Brandon's Forks"))
    db.session.add(Product("Paintbrush", 112, 195, "Art", "An Arts Retailer"))
    db.session.add(Product("Purple Paint", 3, 1995, "Art", "The Paint People"))
    db.session.add(Product("Green Paint", 46, 1995, "Art", "The Paint People"))
    db.session.add(Product("Black Paint", 37, 1795, "Art", "The Paint People"))
    db.session.add(Product("Paper", 1384, 99, "Art", "My Garage"))
    db.session.add(Product("Bowling Ball", 26, 3499, "Sports", "Dicks"))
    db.session.add(Product("Golfing Glove (Left)",16,19995,"Sports","Dicks"))
    db.session.add(Product("Golfing Glove (Right)",18,2499,"Sports","Dicks"))
    db.session.add(Product("Fishing Rod", 37, 2999, "Sports", "My Garage"))
    db.commit()

@app.route('/')
