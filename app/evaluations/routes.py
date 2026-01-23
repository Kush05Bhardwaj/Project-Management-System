from flask import Blueprint

evaluations_bp = Blueprint('evaluations', __name__, url_prefix='/evaluations')

@evaluations_bp.route('/', methods=['GET', 'POST'])
def get_evaluations():
    return {"message": "Evaluations endpoint"}
