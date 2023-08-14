from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.config import DevelopmentConfig
from flask_cors import CORS


db = SQLAlchemy()
migration = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig())
    db.init_app(app)
    migration.init_app(app, db)
    login_manager.init_app(app)
    CORS(app)

    # Register Blueprints here
    from app.routes import plants_bp, auth_bp

    app.register_blueprint(plants_bp, url_prefix="/api")
    app.register_blueprint(auth_bp, url_prefix="/api")

    return app


from app import routes, models
