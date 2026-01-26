from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config
from .logger import setup_logger

jwt = JWTManager()
logger = setup_logger()

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
    

    @app.errorhandler(404)
    def not_found(e):
        return {"message": "Resource not found"}, 404

    @app.errorhandler(500)
    def internal_error(e):
        return {"message": "Internal server error"}, 500

    return app