from flask import Blueprint, jsonify

bp = Blueprint("pages", __name__)

@bp.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})
