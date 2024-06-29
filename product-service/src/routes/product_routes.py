from flask import Blueprint
from controllers.product_controller import create_product, get_product, update_product, delete_product

product_bp = Blueprint('product_bp', __name__)

product_bp.route('/', methods=['POST'])(create_product)
product_bp.route('/<int:id>', methods=['GET'])(get_product)
product_bp.route('/<int:id>', methods=['PUT'])(update_product)
product_bp.route('/<int:id>', methods=['DELETE'])(delete_product)
