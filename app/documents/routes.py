from flask import Blueprint

documents_bp = Blueprint('documents', __name__, url_prefix='/documents')

@documents_bp.route('/', methods=['GET', 'POST'])
def get_documents():
    return {"message": "Documents endpoint"}
