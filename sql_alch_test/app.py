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
    # add all the products
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
    db.session.commit()

@app.route('/')
def root():
    ret = ""
    # set up the categories to be looped through
    categories = db.session.query(Product.category).distinct()
    for cat in categories:
        cat = cat[0]
        ret = ret + display_category(cat)
    return ret

@app.route('/Culinary')
def cul_page():
    return display_category('Culinary')

@app.route('/Art')
def art_page():
    return display_category('Art')

@app.route('/Sports')
def sport_page():
    return display_category('Sports')

def display_category(cat_str):
    ret = "<h1 style=',margin:0px'>" + cat_str + "</h1><br>"
    for p in db.session.query(Product).filter(Product.category == cat_str):
        # name of the Product
        ret = ret + "<strong style='margin:0px;'>" + p.name + "</strong>"
        # information about the Product
        info = "<p style='margin:0px;'>"
        info = info + str(p.num) + " left in stock. $" + dollars(p.price)
        info = info + ". Sold by " + p.seller + "</p><br>"
        ret = ret + info
    return ret

# given an integer for a number of cents, converts into a dollars string
def dollars(cents):
    cents = str(cents)
    return cents[0:-2] + "." + cents[-2] + cents[-1]

if __name__ == '__main__':
    app.debug = True
    app.run('127.0.0.1', 5000)
