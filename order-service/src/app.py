import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from database import db
from routes.order_routes import order_bp

app = Flask(__name__)
CORS(app)

# Configure the database connection
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_NAME = os.environ.get('DATABASE_NAME')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret'

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(order_bp, url_prefix='/orders')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
