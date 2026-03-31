from flask import Blueprint

transaction_bp = Blueprint("transactions", __name__)

@transaction_bp.route("/transactions")
def test():
    return {"ok": True}