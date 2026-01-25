from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from .db import get_db
from .teams.routes import teams_bp


jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    jwt.init_app(app)

    from app.auth.routes import auth_bp
    from app.teams.routes import teams_bp
    from app.documents.routes import documents_bp
    from app.evaluations.routes import evaluations_bp
    
    app.register_blueprint(auth_bp)  # Register only once
    app.register_blueprint(teams_bp)
    app.register_blueprint(documents_bp)
    app.register_blueprint(evaluations_bp)
    
    return app