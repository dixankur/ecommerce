from flask import request, jsonify
from models.order_model import Order
from database import db

def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    total_price = data.get('total_price')
    status = data.get('status')

    if not user_id or not product_id or not quantity or not total_price or not status:
        return jsonify({'error': 'All fields are required'}), 400

    order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price, status=status)
    db.session.add(order)
    db.session.commit()

    return jsonify({'order': order.serialize()}), 201

def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify({'order': order.serialize()}), 200

def update_order(id):
    data = request.get_json()
    status = data.get('status')

    order = Order.query.get_or_404(id)
    order.status = status
    db.session.commit()

    return jsonify({'order': order.serialize()}), 200

def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return '', 204
