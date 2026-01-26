from flask import Blueprint, render_template, redirect, url_for, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from app.db import get_db, get_user_by_email

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = get_user_by_email(email)
        if user and user.check_password(password):
            access_token = create_access_token(identity=user.id)
            return redirect(url_for('ui.dashboard'))
    return render_template('login.html')

@ui_bp.route('/student')
def student_dashboard():
    return render_template('student_dashboard.html')

@ui_bp.route('/mentor')
def mentor_dashboard():
    return render_template('mentor_dashboard.html')

@ui_bp.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')