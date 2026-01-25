from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.db import get_db
from .models import Evaluation
from app.auth.utils import role_required

evaluations_bp = Blueprint("evaluations", __name__, url_prefix='/evaluations')

# Mentor submits evaluation
@evaluations_bp.route("/submit", methods=["POST"])
@jwt_required()
@role_required("mentor")
def submit_evaluation():
    email = get_jwt_identity()  # This is now just the email string
    data = request.json

    team_name = data.get("team_name")
    marks = data.get("marks")
    remarks = data.get("remarks")

    db = get_db()
    team = db.teams.find_one({"name": team_name, "mentor_email": email})

    if not team:
        return jsonify({"msg": "Unauthorized team"}), 403

    eval = Evaluation(team_name, email, marks, remarks)
    db.evaluations.insert_one(eval.__dict__)

    return jsonify({"msg": "Evaluation submitted"}), 201


# Student views their evaluation
@evaluations_bp.route("/my-result", methods=["GET"])
@jwt_required()
@role_required("student")
def student_result():
    email = get_jwt_identity()  # This is now just the email string
    db = get_db()

    team = db.teams.find_one({"students": email})
    if not team:
        return jsonify({"msg": "No team found"}), 404

    evaluation = db.evaluations.find_one({"team_name": team["name"]}, {"_id": 0})
    return jsonify(evaluation), 200


# Admin views all evaluations
@evaluations_bp.route("/all", methods=["GET"])
@jwt_required()
@role_required("admin")
def all_evaluations():
    db = get_db()
    evaluations = list(db.evaluations.find({}, {"_id": 0}))
    return jsonify(evaluations), 200
