from flask import request, jsonify
from models.product_model import Product
from database import db

def create_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')

    if not name or not price or not stock:
        return jsonify({'error': 'Name, price, and stock are required'}), 400

    product = Product(name=name, description=description, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()

    return jsonify({'product': product.serialize()}), 201

def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({'product': product.serialize()}), 200

def update_product(id):
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    version = data.get('version')

    product = Product.query.filter_by(id=id, version=version).first()

    if not product:
        return jsonify({'error': 'Product not found or version mismatch'}), 409

    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if stock:
        product.stock = stock

    product.version += 1
    db.session.commit()

    return jsonify({'product': product.serialize()}), 200

def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
