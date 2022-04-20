from flask import Flask, request, jsonify, make_response,render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema
from flask_marshmallow import Marshmallow
from marshmallow import fields
from settings import db,app,ma


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:testedafiti123@teste-dafiti.cey2lkidksyb.eu-west-1.rds.amazonaws.com:3306/Dafiti'
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'
db = SQLAlchemy(app)
ma = Marshmallow(app)

###Models####
class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    productDescription = db.Column(db.String(100))
    productBrand = db.Column(db.String(20))
    price = db.Column(db.Integer)

    def create(self):
      db.session.add(self)
      db.session.commit()
      return self
    def __init__(self,title,productDescription,productBrand,price):
        self.title = title
        self.productDescription = productDescription
        self.productBrand = productBrand
        self.price = price
    def __repr__(self):
        return '' % self.id
db.create_all()


class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        #sqla_session = db.session
    id = ma.auto_field()
    title = ma.auto_field()
    productDescription = ma.auto_field()
    productBrand = ma.auto_field()
    price = ma.auto_field()
