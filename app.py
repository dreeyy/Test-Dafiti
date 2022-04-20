from flask import Flask, request, jsonify, make_response,render_template
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from forms import SearchForm
from model import Product,ProductSchema
from flask_marshmallow import Marshmallow
from marshmallow import fields
from settings import db,app,ma
import json

@app.route('/products', methods = ['GET'])
def index():
    data = db.session.query(Product).all()
    db.session.commit()
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(data,many=True)    
    return make_response(jsonify({"product": products}))


@app.route('/products', methods = ['POST'])
def create_product():
    data = request.get_json()
    product_schema = ProductSchema()
    product = Product(title=data["title"],productDescription=data["productDescription"],productBrand=data["productBrand"],price=data["price"])
    db.session.add(product)    
    result = product_schema.dump(product)
    db.session.commit()
    return make_response(jsonify({"product": result}),200)


@app.route('/products/<id>', methods = ['PUT'])
def update_product_by_id(id):
    data = request.get_json()
    get_product = db.session.query(Product).get(id)
    if data.get('title'):
        get_product.title = data['title']
    if data.get('productDescription'):
        get_product.productDescription = data['productDescription']
    if data.get('productBrand'):
        get_product.productBrand = data['productBrand']
    if data.get('price'):
        get_product.price= data['price']  

    db.session.add(get_product)
    db.session.commit()
    product_schema = ProductSchema(only=['id', 'title', 'productDescription','productBrand','price'])
    product = product_schema.dump(get_product)
    return make_response(jsonify({"product": product}))

@app.route('/products/<id>', methods = ['DELETE'])
def delete_product_by_id(id):
    get_product = db.session.query(Product).filter_by(id=id).one()
    db.session.delete(get_product)
    db.session.commit()
    return make_response("",204)

@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        return redirect(url_for('search', name=form.username.data))
    return render_template('search.html', form=form)

@app.route('/products/<title>', methods = ['GET'])
def search(title):
    get_products = Product.query.get(title)
    product_schema = ProductSchema(many=True)
    products = product_schema.dump(get_products)
    return make_response(jsonify({"product": products}))

#@app.route('/products/<title>')
#def search(title):
#    data = request.get_json()
#    get_product = Product.query.get(title)

#    info = requests.get('http://localhost:5000/search/'+name)
#    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
#    info = json.loads(info)
#    return render_template('show.html', info=info)


if __name__ == "__main__":
    app.run(debug=True)