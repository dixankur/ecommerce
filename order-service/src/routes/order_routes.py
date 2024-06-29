from flask import Blueprint
from controllers.order_controller import create_order, get_order, update_order, delete_order

order_bp = Blueprint('order_bp', __name__)

order_bp.route('/', methods=['POST'])(create_order)
order_bp.route('/<int:id>', methods=['GET'])(get_order)
order_bp.route('/<int:id>', methods=['PUT'])(update_order)
order_bp.route('/<int:id>', methods=['DELETE'])(delete_order)
