from flask import Blueprint, render_template, jsonify
from flask import request
from app.chat_openai import get_response

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/chat", methods = ["POST"])
def chat():
    user_msg = request.json.get("message")
    resposta = get_response(user_msg)
    return jsonify({"response":resposta})