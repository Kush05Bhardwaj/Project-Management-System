from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from .models import User
from app.db import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'Student')

    db = get_db()
    if db.get_user_by_email(email):
        return jsonify({"message": "User already exists"}), 400
    
    user = User(email, password, role)
    db.users.insert_one(user.__dict__)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    db = get_db()
    user = db.get_user_by_email(email)

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401
    
    temp_user = User(user["email"], password)
    if not temp_user.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401
    
    token = create_access_token(identity={"email": email, "role": user["role"]})
    return jsonify({"access_token": token}), 200