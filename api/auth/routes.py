from flask import request, jsonify, Blueprint
from api.services import db_manager
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from api.utils import (
    exists,
    valid_email,
    generate_acc_number,
    generate_password,
)

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if username is None or password is None:
        return jsonify({"message": "Username and Password are required"}), 400

    # Cria um token de autenticação com o usuário
    token = create_access_token(identity=username, expires_delta=timedelta(hours=2))

    # Retorna o token de autenticação para o usuário
    return jsonify(token=token), 200
