from flask import Flask
from app.routes.transaction_routes import transaction_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(transaction_bp, url_prefix="/api")

    return app