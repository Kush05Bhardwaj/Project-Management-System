from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.db import get_db
from .models import Team
from app.auth.utils import role_required

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')


# Admin creates Teams
@teams_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required("admin")
def create_team():
    data = request.get_json()
    name = data.get('name')
    mentor_email = data.get('mentor_email')

    if not name or not mentor_email:
        return jsonify({"message": "Name and mentor email are required"}), 400

    team = Team(name, mentor_email)
    db = get_db()
    db.teams.insert_one(team.__dict__)
    return jsonify({"message": "Team created successfully"}), 201

# Add Student to team
@teams_bp.route("/add-student", methods=["POST"])
@jwt_required()
@role_required("admin")
def add_student():
    data = request.get_json()
    team_name = data.get('team_name')
    student_email = data.get('student_email')

    if not team_name or not student_email:
        return jsonify({"message": "Team name and student email are required"}), 400

    db = get_db()
    result = db.teams.update_one(
        {"name": team_name},
        {"$addToSet": {"students": student_email}}
    )

    if result.modified_count == 0:
        return jsonify({"message": "Team not found or student already added"}), 404

    return jsonify({"message": "Student added to team successfully"}), 200

# Mentor views their team
@teams_bp.route("/my-team", methods=["GET"])
@jwt_required()
@role_required("student")
def student_team():
    email = get_jwt_identity()  # This is now just the email string
    db = get_db()
    team = db.teams.find_one({"students": email}, {"_id": 0})
    return jsonify(team), 200


