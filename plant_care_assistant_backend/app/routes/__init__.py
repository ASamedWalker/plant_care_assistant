from flask import Blueprint

plants_bp = Blueprint("plants", __name__)
auth_bp = Blueprint("auth", __name__)

from app.routes import plants, auth