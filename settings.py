from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://admin:testedafiti123@teste-dafiti.cey2lkidksyb.eu-west-1.rds.amazonaws.com:3306/Dafiti'
app.config['SECRET_KEY'] = '3141592653589793238462643383279502884197169399'
db = SQLAlchemy(app)
ma = Marshmallow(app)