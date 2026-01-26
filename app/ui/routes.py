from flask import Blueprint, render_template, redirect, url_for, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, get_jwt
from app.db import get_db, get_user_by_email
from app.auth.utils import role_required

ui_bp = Blueprint('ui', __name__)

@ui_bp.route('/')
def index():
    return redirect(url_for('ui.login'))

@ui_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = get_user_by_email(email)
        if not user:
            return render_template('login.html', error="Invalid credentials")
        
        # Import User model to check password
        from app.auth.models import User
        # Create temporary user object with the stored password hash
        temp_user = User(user["email"], user["password_hash"])
        temp_user.password_hash = user["password_hash"]  # Set the stored hash
        
        # Check if entered password matches the stored hash
        if not temp_user.check_password(password):
            return render_template('login.html', error="Invalid credentials")
        
        # Create access token
        access_token = create_access_token(identity=email, additional_claims={"role": user["role"]})
        
        # Redirect based on role
        response = None
        if user["role"] == "student":
            response = redirect(url_for('ui.student_dashboard'))
        elif user["role"] == "mentor":
            response = redirect(url_for('ui.mentor_dashboard'))
        elif user["role"] == "admin":
            response = redirect(url_for('ui.admin_dashboard'))
        else:
            return render_template('login.html', error="Invalid role")
        
        # Set JWT token as cookie (for browser-based access)
        response.set_cookie('access_token_cookie', access_token)
        return response
        
    return render_template('login.html')

@ui_bp.route('/student')
@jwt_required()
@role_required('student')
def student_dashboard():
    db = get_db()
    email = get_jwt_identity()  # This is now just the email string

    team = db.teams.find_one({"students": email})
    docs = []
    result = None

    if team:
        docs = list(db.documents.find({"team_name": team["name"]}))
        result = db.evaluations.find_one({"team_name": team["name"]}, {"_id": 0})

    return render_template('dashboard_student.html', team=team, docs=docs, result=result)

@ui_bp.route('/mentor')
@jwt_required()
@role_required('mentor')
def mentor_dashboard():
    db = get_db()
    email = get_jwt_identity()  # This is now just the email string

    teams = list(db.teams.find({"mentor_email": email}))
    docs = list(db.documents.find({"team_name": {"$in": [team["name"] for team in teams]}}, {"_id": 0}))
    return render_template('dashboard_mentor.html')

@ui_bp.route('/admin')
@jwt_required()
@role_required('admin')
def admin_dashboard():
    return render_template('dashboard_admin.html')

@ui_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload_ui():
    from app.documents.routes import upload_documents
    return upload_documents()

@ui_bp.route('/review', methods=['POST'])
@jwt_required()
def review_ui():
    from app.documents.routes import review_documents
    return review_documents()