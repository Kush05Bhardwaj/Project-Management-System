from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    return {"message": "Login endpoint"}

@auth_bp.route('/register', methods=['POST'])
def register():
    return {"message": "Register endpoint"}

@auth_bp.route('/logout', methods=['POST'])
def logout():   
    return {"message": "Logout endpoint"}