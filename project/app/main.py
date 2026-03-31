from flask import Flask


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "dev"

    # Importa e registra rotas
    from app.routes.transaction_routes import transaction_bp
    app.register_blueprint(transaction_bp, url_prefix="/api")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
