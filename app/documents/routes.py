import os
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from app.db import get_db
from .models import Document
from app.auth.utils import role_required

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

documents_bp = Blueprint('documents', __name__, url_prefix='/documents')


# Student uploads documents
@documents_bp.route('/upload', methods=['POST'])
@jwt_required()
@role_required("student")
def upload_documents():
    email = get_jwt_identity()  # This is now just the email string
    file = request.files.get("file")

    if not file:
        return jsonify({"msg": "No file uploaded"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    db = get_db()
    team = db.teams.find_one({"students": email})
    if not team:
        return jsonify({"msg": "Student not in any team"}), 400

    doc = Document(filename, email, team["name"])
    db.documents.insert_one(doc.__dict__)

    return jsonify({"msg": "File uploaded", "status": doc.status}), 201


# Mentor views documents of their teams
@documents_bp.route("/mentor/docs", methods=["GET"])
@jwt_required()
@role_required("mentor")
def mentor_docs():
    email = get_jwt_identity()  # This is now just the email string
    db = get_db()

    teams = db.teams.find({"mentor_email": email})
    team_names = [t["name"] for t in teams]

    docs = list(db.documents.find({"team_name": {"$in": team_names}}, {"_id": 0}))
    return jsonify(docs), 200


# Mentor approves/rejects document
@documents_bp.route("/review", methods=["POST"])
@jwt_required()
@role_required("mentor")
def review_doc():
    data = request.json
    filename = data.get("filename")
    status = data.get("status")  # approved / rejected
    comment = data.get("comment", "")

    db = get_db()
    db.documents.update_one(
        {"filename": filename},
        {"$set": {"status": status, "review_comment": comment}}
    )

    return jsonify({"msg": f"Document {status}"}), 200