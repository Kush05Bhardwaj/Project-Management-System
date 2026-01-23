from flask import Blueprint

teams_bp = Blueprint('teams', __name__, url_prefix='/teams')

@teams_bp.route('/', methods=['GET', 'POST'])
def get_teams():
    return {"message": "Teams endpoint"}
